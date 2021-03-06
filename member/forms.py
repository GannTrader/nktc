from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from member.models import Student


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'Tên đăng nhập...'
            })),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email...'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mật khẩu...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu...'})


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['avatar', 'address', 'phone']

        widgets = {
            'address': forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'Địa chỉ sinh sống hoặc làm việc...'
            })),
            'phone': forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'Số điện thoại liên hệ...'
            }))
        }