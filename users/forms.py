from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit

from .models import User

class CreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # this line sets your form's method to post
        self.helper.layout = Layout( # the order of the items in this layout is important
            'username',
            'email',
            'password1',
            'password2',
            # this is how to add the submit button to your form and since it is the last item in this tuple, it will be rendered last in the HTML
            Submit('submit', u'Submit', css_class='btn btn-info'),
        )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
