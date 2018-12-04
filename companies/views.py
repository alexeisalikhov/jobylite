from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import CompanyCreationForm
from .models import Company

@method_decorator(login_required, name='dispatch')
class CompanyCreateForm(CreateView):
    form_class = CompanyCreationForm
    template_name = 'create.html'
    # view way of passing extra context, less preferable
    model_name = form_class.Meta.model._meta.verbose_name

    # context to facilite using the same template
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['templata'] = 'Company'
    #     return context


    def form_valid(self, form):
        response = super().form_valid(form)
        # Add user to created company
        self.object.users.add(self.request.user)
        # Set created company as user's current company
        self.request.user.company = self.object
        self.request.user.save()
        logo = form.cleaned_data['logo']
        return super().form_valid(form)


class CompanyDeleteView(DeleteView):
    # form_class = JobCreationForm
    model = Company
    template_name = 'delete.html'
    success_url = reverse_lazy('companies:list')


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company.html'


class CompanyListView(ListView):
    model = Company
    template_name = 'companies.html'


class CompanyUpdateView(UpdateView):
    form_class = CompanyCreationForm
    model = Company
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('companies:detail', kwargs={'pk': self.object.id})
