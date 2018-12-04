from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models

# from companies.models import Company
from times.models import TimeStampedModel



class User(AbstractUser, TimeStampedModel):
    # First/last name is not a global-friendly pattern
    # name = models.CharField(max_length=255, blank=True)
    # current_company = models.ForeignKey('Company', on_delete=models.SET_NULL)


    def __str__(self):
        return self.email
