from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ChangeForm
from .forms import CreationForm
from .models import User

class Admin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = User
    list_display = ['email', 'username']

admin.site.register(User, Admin)
