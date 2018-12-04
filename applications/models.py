from django.db import models
from django.urls import reverse

from jobs.models import Job
from times.models import TimeStampedModel
from users.models import User


class Application(TimeStampedModel):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='photos')
    cv = models.FileField(blank=True, upload_to='cvs')
    doc = models.FileField(blank=True, upload_to='docs')
    text = models.TextField(blank=True)
    is_evaluated = models.BooleanField(blank=True, default=False)
    is_candidate = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('applications:thankyou')
