# Generated by Django 5.1.4 on 2025-01-06 11:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_otpcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/images/'),
        ),
    ]
