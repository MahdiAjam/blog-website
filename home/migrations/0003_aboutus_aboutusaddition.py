# Generated by Django 5.1.4 on 2024-12-26 17:44

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactinformation_contactinformationphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/images/')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsAddition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='about/images/')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additions', to='home.aboutus')),
            ],
        ),
    ]