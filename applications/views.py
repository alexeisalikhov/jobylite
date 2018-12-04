from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView

from .forms import ApplicationCreationForm
from applications.models import Application
from jobs.models import Job


class ApplicationCreateForm(CreateView):
    form_class = ApplicationCreationForm
    template_name = 'applicationcreation.html'
    model_name = form_class.Meta.model._meta.verbose_name

    def form_valid(self, form):
        form.instance.job_id = self.kwargs.get('job_id')
        photo = form.cleaned_data['photo']
        doc = form.cleaned_data['doc']
        cv = form.cleaned_data['cv']
        return super().form_valid(form)


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'application.html'

    def post(self, request, *args, **kwargs):
        application = self.get_object()
        email = self.request.POST.get('inlineRadioOptions')
        if email == 'Yes':
            self.send_yes_email(application)
            application.is_evaluated = True
            application.is_candidate = True
            application.save()
        elif email == 'No':
            self.send_no_email(application)
            application.is_evaluated = True
            application.save()
        else:
            raise IOError('Not supported input')
        return redirect('jobs:detail', pk=application.job.id)

    def send_yes_email(self, application):
        yes_message = "You're in!"
        send_mail(
            'Regarding ' + application.job.title,
            yes_message,
            application.job.company.email,
            [application.email],
            fail_silently=False,
        )

    def send_no_email(self, application):
        no_message = "It's a no. Good luck with your other applications!"
        send_mail(
            'Regarding ' + application.job.title,
            no_message,
            application.job.company.email,
            [application.email],
            fail_silently=False,
        )


    # IMPLEMENT FORM SET LATER
    # FormSet = modelformset_factory(Application)
    # Form = modelform_factory(Job)
    #
    # def myview(request):
    #     formset = FormSet(request.POST or None)
    #     form = Form(request.POST or None)
    #
    #     if request.method == 'POST':
    #         if formset.is_valid() and form.is_valid():
    #             main_instance = form.save()
    #             formset.save(commit=False)
    #             for instance in formset:
    #                 instance.fk = main_instance
    #                 instance.save()


def thankyou(request):
    return render(request, 'thankyou.html')
