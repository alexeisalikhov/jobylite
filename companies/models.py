from django.urls import reverse
from django.db import models

from ckeditor.fields import RichTextField

# from commons.models import NameMixin
from jobysite.settings import AUTH_USER_MODEL
from times.models import TimeStampedModel
from users.models import User


class Company(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = RichTextField(max_length=5000, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    logo = models.ImageField(blank=True, upload_to='logos')
    users = models.ManyToManyField(User)
    # related_name limitations now: no User.company_set
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='+')

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companies:list')


# class Job(NameMixin, TimeStampedModel):
#     title = models.CharField(max_length=200)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     description = models.TextField(max_length=1000, blank=True)
#     # A list of questions separated by commas (will receive own fields in Application)
#     questions = ArrayField(models.CharField(blank=True, max_length=200), size=6)
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('company')


# class Applicant(NameMixin, TimeStampedModel):
#     name = models.CharField(max_length=200)
#     question = models.TextField
#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#     photo = models.ImageField(blank=True, upload_to='photos/')
#     cv = models.FileField(blank=True, upload_to='cvs/')
#     doc = models.FileField(blank=True, upload_to='docs/')
#     text = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name
