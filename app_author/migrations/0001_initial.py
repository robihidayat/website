# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 08:28
from __future__ import unicode_literals

import app_author.models
import autoslug.fields
import datetime
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', validators=[app_author.models.validate_image])),
                ('profile_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('profile_email', models.EmailField(blank=True, help_text='Masukan alamat email kamu', max_length=254, null=True, verbose_name='Email Address')),
                ('profile_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Origin/City')),
                ('profile_github', models.URLField(blank=True, null=True, verbose_name='Github URL')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user')),
                ('is_created', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('is_moderator', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
