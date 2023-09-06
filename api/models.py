from django.db import models

# Create your models here.

class Link(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    updatedValue=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def _str_(self):
        return self.title[0:50]


class Advantage(models.Model):
    one=models.CharField(max_length=100, null=True, blank=True)
    two=models.CharField(max_length=100, null=True, blank=True)
    three=models.CharField(max_length=100, null=True, blank=True)
    updatedValue=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(null=True, blank=True, auto_now_add=True)
    

    def __str__(self):
        return self.one    