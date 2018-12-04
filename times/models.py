from datetime import datetime

from django.db import models


# Maybe no need to have it in separate app?
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # accessed.. one can use modified

    class Meta:
        abstract = True
