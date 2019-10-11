from django import forms
from django.utils.translation import gettext_lazy as _

# 登录验证表单
class LoginForm(forms.Form):
    username = forms.CharField(label='username', required=True)
    password = forms.CharField(label='password', required=True)

# 注册验证表单
class SignUpForm(forms.Form):
    username = forms.CharField(label='username', required=True)
    nickname = forms.CharField(label='nickname', required=True)
    password = forms.CharField(label='password', required=True)
    confirm_password = forms.CharField(label='confirm_password', required=True)

