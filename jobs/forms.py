from django import forms
from django.contrib.postgres.forms import SplitArrayField
from django.contrib.postgres.forms import SplitArrayWidget
from django.db import models
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit

from .models import Job


class JobCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # this line sets your form's method to post
        self.helper.layout = Layout( # the order of the items in this layout is important
            'title',
            'description',
            Submit('submit', u'Submit', css_class='btn btn-success'),
        )

    # def __init__(self, *args, **kwargs):
    #
    #     super().__init__(*args, **kwargs)
    #
    #     # field 'questions'
    #     widget_base_field = self.fields['questions'].base_field.widget
    #     count_inputs = self.fields['questions'].max_length
    #     self.fields['questions'].widget = SplitInputsArrayWidget(
    #         widget_base_field,
    #         count_inputs,
    #         remove_trailing_nulls=True,
    #         attrs={'class': 'span12'}
    #     )

    class Meta:
        model = Job
        fields = ['title', 'description']



# class SplitInputsArrayWidget(SplitArrayWidget):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def value_from_datadict(self, data, files, name):
#
#         value_from_datadict = super().value_from_datadict(data, files, name)
#
#         # convert a list to a string, with commas-separated values
#         value_from_datadict = ','.join(value_from_datadict)
#
#         return value_from_datadict
#
#     def render(self, name, value, attrs=None):
#
#         # if object has value, then
#         # convert a sting to a list by commas between values
#         if value is not None:
#             value = value.split(',')
#
#         return super().render(name, value, attrs=None)
