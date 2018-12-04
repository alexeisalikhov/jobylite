from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit

from .models import Company
# from .models import Job


class CompanyCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # this line sets your form's method to post
        self.helper.layout = Layout( # the order of the items in this layout is important
            'logo',
            'name',
            'description',
            'website',
            'email',

            Submit('submit', u'Submit', css_class='btn btn-success'),
        )

    class Meta:
        model = Company
        fields = ['name', 'description', 'website', 'email', 'logo']


# class JobCreationForm(ModelForm):
#
#     class Meta:
#         model = Job
#         fields = ['title', 'description', 'questions']
