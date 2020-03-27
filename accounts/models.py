from django.db import models


# Create your models here.
class Learner(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=8)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
