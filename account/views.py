from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, VerifyCodeForm
from .models import OtpCode, User
import random
from utils import send_otp_code
from django.contrib import messages


class RegisterView(View):
    template_name = 'account/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you the code', 'success')
            return redirect('account:verify_code')
        return render(request, self.template_name, {'form': form})


class RegisterVerifyCode(View):
    form_class = VerifyCodeForm
    template_name = 'account/verify.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['full_name'], user_session['password'])
                code_instance.delete()
                messages.success(request, 'you registered.', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'this code is wrong', 'danger')
                return redirect('account:verify_code')
        return redirect('home:home')


class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name)
