from django.shortcuts import render, redirect
from django.views import View
from .models import ContactInformation, AboutUs
from .forms import ContactUsForm
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request):
        about_us = AboutUs.objects.all()
        return render(request, self.template_name, {'about': about_us})

class ContactView(View):
    form_class = ContactUsForm
    template_name = 'home/contact.html'

    def get(self, request):
        contact_information = ContactInformation.objects.all()
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'contact': contact_information})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your message send.', 'success')
            return redirect('home:contact')
        return render(request, self.template_name, {'form': form})
