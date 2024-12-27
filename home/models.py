from django.db import models
from ckeditor.fields import RichTextField

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}-{self.subject}'


class ContactInformation(models.Model):
    email = models.EmailField()
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email}-{self.city}'


class ContactInformationPhone(models.Model):
    contact = models.ForeignKey(ContactInformation, on_delete=models.CASCADE, related_name='phones')
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.phone}'

class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/images/')
    description = RichTextField

    def __str__(self):
        return 'this is the about us'

class AboutUsAddition(models.Model):
    contact = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='additions')
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='about/images/')

    def __str__(self):
        return f'{self.title}'
