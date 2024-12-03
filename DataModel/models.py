# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models





# Create your models here.
class Field(models.Model):
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)
    parent_field = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    model = models.CharField(max_length=100, null= True, blank= True)

    def __str__(self):
        return self.field_name
