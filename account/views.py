from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserRegisterForm, VerifyCodeForm, UserLoginForm, UserEditProfileForm
from .models import OtpCode, User, Relation
import random
from utils import send_otp_code
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy


class UserRegisterView(View):
    template_name = 'account/register.html'
    form_class = UserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'you already logged in.', 'warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'you already logged in.', 'warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

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


class UserLoginView(View):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'you already logged in.', 'warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
            messages.error(request, 'your phone or password are wrong', 'warning')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'account/profile.html'

    def get(self, request, pk):
        is_following = False
        author = get_object_or_404(User, pk=pk)
        article = author.authors.all()
        paginator = Paginator(article, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        relation = Relation.objects.filter(from_user=request.user, to_user=author)
        if relation.exists():
            is_following = True
        return render(request, self.template_name, {'author': author, 'article': page_obj, 'is_following': is_following})


class UserEditProfileView(LoginRequiredMixin, View):
    template_name = 'account/edit_profile.html'
    form_class = UserEditProfileForm

    def get(self, request, pk=None):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk=None):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile edited successfully', 'success')
            return redirect('account:user profile', request.user.id)
        return render(request, self.template_name, {'form': form})


class UserPasswordResetView(auth_view.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password reset done')
    email_template_name = 'account/password_reset_email.html'


class UserPasswordDoneView(auth_view.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(auth_view.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password reset complete')


class UserPasswordResetCompleteView(auth_view.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        author = User.objects.get(id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=author)
        if relation.exists():
            messages.error(request, f'you already follow {author.full_name}', 'danger')
        else:
            Relation(from_user=request.user, to_user=author).save()
            messages.success(request, f'you follow {author.full_name}', 'success')
        return redirect('account:user profile', author.id)


class UserUnFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        author = User.objects.get(id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=author)
        if relation.exists():
            relation.delete()
            messages.success(request, f'you unfollow {author.full_name}', 'success')
        else:
            messages.error(request, f'you are not follow {author.full_name}', 'danger')
        return redirect('account:user profile', author.id)
