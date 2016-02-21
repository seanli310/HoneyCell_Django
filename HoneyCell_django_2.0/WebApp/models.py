from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


def generate_filename(self, filename):

    print(self.date)
    print(self.date.date().year)
    print(self.date.date().month)
    print(self.date.date().day)

    url = 'documents/%s/%s/%s/%s' %(self.user.username, self.folder, self.label, filename)
    return url


class Document(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    folder = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=100, blank=True)
    docfile = models.FileField(upload_to=generate_filename)
    date = models.DateTimeField(default=timezone.now)