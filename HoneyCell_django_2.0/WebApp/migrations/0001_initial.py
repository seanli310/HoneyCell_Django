# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 19:09
from __future__ import unicode_literals

import WebApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm_name', models.CharField(max_length=100)),
                ('algorithm_description', models.TextField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=100)),
                ('folder_time_created', models.DateTimeField(auto_now_add=True)),
                ('folder_time_changed', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Followship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_datetime', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_is_followed', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_follows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=100)),
                ('label_description', models.TextField(max_length=1000)),
                ('label_time_created', models.DateTimeField(auto_now_add=True)),
                ('label_time_changed', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=100)),
                ('short_introduction', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to=WebApp.models.generate_url_images)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_changed', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
                ('status_description', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('docfile', models.FileField(upload_to=WebApp.models.generate_filename)),
                ('task_time_created', models.DateTimeField(auto_now_add=True)),
                ('task_time_changed', models.DateTimeField(auto_now=True)),
                ('input_file_address', models.CharField(default='', max_length=100)),
                ('output_file_address', models.CharField(default='', max_length=100)),
                ('task_algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Algorithm')),
                ('task_folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Folder')),
                ('task_label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.Label')),
                ('task_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskPending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Task')),
                ('task_status', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='task',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.Task'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
