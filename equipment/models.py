from django.db import models

# Create your models here.
import uuid
from django.utils import timezone
from django.db import models


class Data(models.Model):
    data_created = models.DateTimeField(default=timezone.now)
    power = models.DecimalField(blank=True, max_digits=3, decimal_places=1)
    equipment = models.CharField(max_length=50)
    status = models.BooleanField()

    class Meta:
        ordering = ['data_created']
