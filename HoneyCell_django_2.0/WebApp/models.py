from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

class Folder(models.Model):
    user = models.ForeignKey(User)
    folder_name = models.CharField(max_length=100)
    folder_time_created = models.DateTimeField(auto_now_add=True)
    folder_time_changed = models.DateTimeField(auto_now=True)

class Label(models.Model):
    label_name = models.CharField(max_length=100)
    label_description = models.TextField(max_length=1000)


# Later we need to change this status, not bind to user
class Status(models.Model):
    user = models.ForeignKey(User)
    status_name = models.CharField(max_length=100)
    status_description = models.CharField(max_length=1000)

# Later we need to change this status, not bind to user
class Algorithm(models.Model):
    algorithm_name = models.CharField(max_length=100)
    algorithm_description = models.TextField(max_length=1000)

def generate_training_filename(self, filename):
    url = 'documents/%s/%s/trainings/%s' %(self.user.username, self.task_folder.folder_name, filename)
    return url

def generate_testing_filename(self, filename):
    url = 'documents/%s/%s/testings/%s' %(self.user.username, self.task_folder.folder_name, filename)
    return url

class Task(models.Model):
    user = models.ForeignKey(User)
    task_name = models.CharField(max_length=100)
    task_algorithm = models.ForeignKey(Algorithm)
    task_description = models.TextField(max_length=1000, null=True, blank=True)
    task_folder = models.ForeignKey(Folder)
    task_label = models.ForeignKey(Label, null=True, blank=True)
    task_status = models.ForeignKey(Status)

    # upload two files, training file and testing file
    training_docfile = models.FileField(upload_to=generate_training_filename)
    testing_docfile = models.FileField(upload_to=generate_testing_filename)

    task_time_created = models.DateTimeField(auto_now_add=True)
    task_time_changed = models.DateTimeField(auto_now=True)
    input_file_address = models.CharField(default="", max_length=100)
    output_file_address = models.CharField(default="", max_length=100)

    def __unicode__(self):
        return "%s by %s" %(self.task_name, self.user.username)

#  used when checking task status by Ajax
class Pending2CompletedTask(models.Model):
    user = models.ForeignKey(User)
    task = models.OneToOneField(Task)

    def __unicode__(self):
        return str(self.task)


class Activity(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField(max_length=1000)
    # Activity object has foreign key Task object, and the foreign key can be null
    task = models.OneToOneField(Task, null=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s, %s" %(self.user.username, self.description)

def generate_url_images(self, filename):
    url = 'images/%s/%s' %(self.user.username, filename)
    return url

class Profile(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(blank=True, max_length=100)
    location = models.CharField(blank=True, max_length=100)
    website = models.URLField(blank=True, max_length=100)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=100)
    short_introduction = models.TextField(blank=True, max_length=1000)
    image = models.ImageField(blank=True, upload_to=generate_url_images)
    time_created = models.DateTimeField(auto_now_add=True)
    time_changed = models.DateTimeField(auto_now=True)

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


