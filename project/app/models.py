from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    number = models.IntegerField()
    title = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self):
        return self.name
