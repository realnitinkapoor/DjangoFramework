from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    updatedtimestamp = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.email
