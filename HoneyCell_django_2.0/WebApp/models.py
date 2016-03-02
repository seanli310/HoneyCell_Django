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


class Task(models.Model):
    task_id = models.AutoField(primary_key=True, blank=True)
    user_id = models.ForeignKey(
            User, on_delete=models.CASCADE,
            related_name="tasks"
    )
    TASK_IMPORTANCE = (
        ('0', 'Important'),
        ('1', 'Warning'),
        ('2', 'Information'),
    )
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=200)
    creat_time = models.DateTimeField(default=timezone.now)
    finish_time = models.DateTimeField(default=timezone.now)
    input_file_address = models.CharField(max_length=100)
    output_file_address = models.CharField(max_length=100)



class Followship(models.Model):
    following = models.ForeignKey(User, related_name="who_follows")
    follower = models.ForeignKey(User, related_name="who_is_followed")
    follow_datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s follows %s at %s" %(self.following, self.follower, self.follow_datetime)

