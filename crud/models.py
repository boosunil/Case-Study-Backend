from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    name = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=400)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name
