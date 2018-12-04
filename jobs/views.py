from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import JobCreationForm
from companies.models import Company
from jobs.models import Job


class JobCreateForm(CreateView):
    form_class = JobCreationForm
    template_name = 'create.html'
    model_name = form_class.Meta.model._meta.verbose_name

    def form_valid(self, form):
        # Set company
        form.instance.company_id = self.kwargs.get('company_id')
        # form.instance.job = self.object
        # form.instance.save()
        return super().form_valid(form)


class JobDeleteView(DeleteView):
    # form_class = JobCreationForm
    model = Job
    template_name = 'delete.html'
    success_url = reverse_lazy('companies:list')


class JobDetailView(DetailView):
    model = Job
    template_name = 'job.html'


class JobUpdateView(UpdateView):
    model = Job
    # instead of declaring fields
    form_class = JobCreationForm
    template_name = 'update.html'
