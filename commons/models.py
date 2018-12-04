from django.db import models

# Create your models here.
class NameMixin(models.Model):

    def model_name(self):
        return self.__class__.__name__

    class Meta:
        abstract = True
