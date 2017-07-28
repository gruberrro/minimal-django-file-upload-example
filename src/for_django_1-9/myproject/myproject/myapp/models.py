# -*- coding: utf-8 -*-
from django.db import models

from django_antivirus_field import ProtectedFileField


class Document(models.Model):
    # instead of using FileField use ProtectedFileField
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile = ProtectedFileField(upload_to='documents/%Y/%m/%d')
