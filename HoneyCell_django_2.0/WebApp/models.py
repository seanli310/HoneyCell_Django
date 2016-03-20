from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


def generate_filename(self, filename):
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

class Folder(models.Model):
    user = models.ForeignKey(User)
    folder_name = models.CharField(max_length=100)
    folder_description = models.TextField(max_length=1000)
    folder_time_created = models.DateTimeField(auto_now_add=True)
    folder_time_changed = models.DateTimeField(auto_now=True)

class Label(models.Model):
    user = models.ForeignKey(User)
    label_name = models.CharField(max_length=100)
    label_description = models.TextField(max_length=1000)
    label_time_created = models.DateTimeField(auto_now_add=True)
    label_time_changed = models.DateTimeField(auto_now=True)

class Task(models.Model):
    user = models.ForeignKey(User)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=1000)
    task_folder = models.ForeignKey(Folder)
    task_label = models.ForeignKey(Label)
    docfile = models.FileField(upload_to=generate_filename)
    task_time_created = models.DateTimeField(auto_now_add=True)
    task_time_changed = models.DateTimeField(auto_now=True)
    input_file_address = models.CharField(default=None, max_length=100)
    output_file_address = models.CharField(default=None, max_length=100)

    def __unicode__(self):
        return "%s by %s" %(self.task_name, self.user.username)


class Activity(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    user = models.OneToOneField(User)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "%s, %s, %s" %(self.street, self.city, self.state)


def generate_url_images(self, filename):
    url = 'images/%s/%s' %(self.user.username, filename)
    return url

class Profile(models.Model):
    user = models.ForeignKey(User)
    company = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    short_introduction = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=generate_url_images)

class Comment(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    text = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)


class Followship(models.Model):
    following = models.ForeignKey(User, related_name="who_follows")
    follower = models.ForeignKey(User, related_name="who_is_followed")
    follow_datetime = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s follows %s at %s" %(self.following, self.follower, self.follow_datetime)

