from django.shortcuts import render
from django.views import View
from .forms import RegisterForm

class RegisterView(View):
    template_name = 'account/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name)
