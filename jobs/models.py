from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

# from commons.models import NameMixin
from companies.models import Company
from times.models import TimeStampedModel
from users.models import User


class Job(TimeStampedModel):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = RichTextField(max_length=5000, blank=True)
    # A list of questions (will receive own fields in Application)
    # questions = ArrayField(
    #     models.CharField(blank=True, max_length=200),
    #     size=3,
    #     blank=True,
    # )
    # question = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'pk': self.id})
