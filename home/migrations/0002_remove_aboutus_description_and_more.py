# Generated by Django 5.1.4 on 2024-12-27 13:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='description',
        ),
        migrations.AlterField(
            model_name='aboutusaddition',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
