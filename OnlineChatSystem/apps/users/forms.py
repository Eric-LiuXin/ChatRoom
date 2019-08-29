from django import forms
from django.utils.translation import gettext_lazy as _

# 登录验证表单
class LoginForm(forms.Form):
    username = forms.CharField(label='username', required=True)
    password = forms.CharField(label='password', required=True)

# 登录验证表单
class SignUpForm(forms.Form):
    usernamesignup = forms.CharField(label='usernamesignup', required=True)
    emailsignup = forms.CharField(label='emailsignup', required=True)
    passwordsignup = forms.CharField(label='passwordsignup', required=True)
    passwordsignup_confirm = forms.CharField(label='passwordsignup_confirm', required=True)

