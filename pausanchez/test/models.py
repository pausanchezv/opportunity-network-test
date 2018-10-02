# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Publication(models.Model):

    username = models.CharField('Username', max_length=20)
    email = models.EmailField('Email', max_length=50)
    note = models.TextField('Note')

    def __str__(self):
        return "{} - {} - {}".format(self.username, self.email, self.note)
