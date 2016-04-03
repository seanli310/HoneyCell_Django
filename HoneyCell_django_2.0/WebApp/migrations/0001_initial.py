# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import WebApp.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=1000)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algorithm_name', models.CharField(max_length=100)),
                ('algorithm_description', models.TextField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=1000)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(to='WebApp.Activity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folder_name', models.CharField(max_length=100)),
                ('folder_time_created', models.DateTimeField(auto_now_add=True)),
                ('folder_time_changed', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Followship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow_datetime', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(related_name='who_is_followed', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(related_name='who_follows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_name', models.CharField(max_length=100)),
                ('label_description', models.TextField(max_length=1000)),
                ('label_time_created', models.DateTimeField(auto_now_add=True)),
                ('label_time_changed', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pending2CompletedTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=100, blank=True)),
                ('location', models.CharField(max_length=100, blank=True)),
                ('website', models.URLField(max_length=100, blank=True)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=100)),
                ('short_introduction', models.TextField(max_length=1000, blank=True)),
                ('image', models.ImageField(upload_to=WebApp.models.generate_url_images, blank=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_changed', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(max_length=100)),
                ('status_description', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=100)),
                ('task_description', models.TextField(max_length=1000, null=True, blank=True)),
                ('training_docfile', models.FileField(upload_to=WebApp.models.generate_training_filename)),
                ('testing_docfile', models.FileField(upload_to=WebApp.models.generate_testing_filename)),
                ('task_time_created', models.DateTimeField(auto_now_add=True)),
                ('task_time_changed', models.DateTimeField(auto_now=True)),
                ('input_file_address', models.CharField(default='', max_length=100)),
                ('output_file_address', models.CharField(default='', max_length=100)),
                ('task_algorithm', models.ForeignKey(to='WebApp.Algorithm')),
                ('task_folder', models.ForeignKey(to='WebApp.Folder')),
                ('task_label', models.ForeignKey(blank=True, to='WebApp.Label', null=True)),
                ('task_status', models.ForeignKey(to='WebApp.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pending2completedtask',
            name='task',
            field=models.OneToOneField(to='WebApp.Task'),
        ),
        migrations.AddField(
            model_name='pending2completedtask',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='task',
            field=models.OneToOneField(null=True, to='WebApp.Task'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
