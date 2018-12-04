from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import HTML
from crispy_forms.layout import Submit

from django.urls import reverse_lazy

from .models import Application
from .models import Job


class ApplicationCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # this line sets your form's method to post
        self.helper.form_action = reverse_lazy('applications:thankyou') # this line sets the form action
        self.helper.layout = Layout( # the order of the items in this layout is important
            'name',
            'email',
            'text',
            'photo',
            'cv',
            'doc',
            Submit('submit', u'Submit', css_class='btn btn-success'),
        )


    class Meta:
        model = Application
        fields = ['name', 'email', 'text', 'photo', 'cv', 'doc']
