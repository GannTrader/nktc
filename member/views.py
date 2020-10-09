from django import forms
from django.contrib.auth import login, password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView

from member.forms import SignupForm
from member.tokens import account_activation_token
from django.utils.translation import gettext, gettext_lazy as _


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/notice-page.html')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'registration/thankyou-page.html')
    else:
        return HttpResponse('Activation link is invalid!')


class EditLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Tên đăng nhập của bạn hoặc gmail...'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Mật khẩu của bạn....'}),
    )


class SiteLoginView(LoginView):
    model = User
    form_class = EditLoginForm
    template_name = "registration/login.html"


class ProfileView(TemplateView):
    template_name = "registration/profile.html"


class SiteLogoutView(LogoutView):
    template_name = "registration/logout.html"


# user change password
class EditPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mật khẩu cũ...'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mật khẩu mới...'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu mới...'})


class SitePasswordChangeView(PasswordChangeView):
    form_class = EditPasswordChangeForm
    template_name = 'password/password_change_form.html'
    success_url = reverse_lazy('password-change-done')


class SitePasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "password/password_change_done.html"


# user reset password
class EditPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control',
                                       'placeholder': 'Nhập chính xác email của bạn để nhận link...'})
    )


class SitePasswordResetView(PasswordResetView):
    email_template_name = 'password/password_reset_email.html'

    form_class = EditPasswordResetForm
    template_name = "password/password_reset_form.html"
    success_url = reverse_lazy("password-reset-done")


class SitePasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password/password_reset_done.html'


class EditSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Nhập mật khẩu mới...'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu mới...'}),
    )

class SitePasswordResetConfirmView(PasswordResetConfirmView):
    form_class = EditSetPasswordForm
    template_name = 'password/password_reset_confirm.html'
    success_url = reverse_lazy('password-reset-complete')


class SitePasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password/password_reset_complete.html'
