from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100, null=True)
    share = models.IntegerField(null=True)
    size = models.IntegerField(null=True)

    def __str__(self):
        return category
