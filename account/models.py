from django.db import models

# Create your models here.

class Information(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f"Information of {self.name}"
