from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, SignUpForm
import json
from users.models import User
from django.contrib.auth.hashers import make_password


def user_login(request):
    redirect_to = request.GET.get('next', '/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                # 登录
                login(request, user)

                return HttpResponse(json.dumps({"success": True}))
            else:
                return HttpResponse(json.dumps({"success": False, 'message': ["用户名密码验证失败！",]}))
        else:
            err_meg = json.loads(form.errors.as_json())
            message = list()
            err_dict = {'username': '用户名', 'password': '密码',}
            for key in err_meg:
                for err in err_meg[key]:
                    message.append("%s: %s" % (err_dict[key], err["message"]))
            return HttpResponse(json.dumps({"success": False, 'message': message}))
    elif request.method == 'GET':
        return render(request, 'users/login.html', {'redirect_to': redirect_to})

def user_sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            usernamesignup = form.cleaned_data['usernamesignup']
            emailsignup = form.cleaned_data['emailsignup']
            passwordsignup = form.cleaned_data['passwordsignup']
            passwordsignup_confirm = form.cleaned_data['passwordsignup_confirm']

            if passwordsignup != passwordsignup_confirm:
                return JsonResponse({'success': False, 'msg': '两次输入密码不一致'})
            elif User.objects.filter(username=usernamesignup):
                return JsonResponse({'success': False, 'msg': '该账号已存在'})
            elif User.objects.filter(email=emailsignup):
                return JsonResponse({'success': False, 'msg': '该邮箱已被注册'})

            try:
                user = User(
                    username = usernamesignup,
                    email=emailsignup,
                    password=make_password(passwordsignup)
                )
                user.save()
            except Exception as e:
                return JsonResponse({'success':False, 'msg':'服务器创建用户失败', 'detail':repr(e)})

            return JsonResponse({'success': True, 'msg': '用户创建成功，请登录'})
        else:
            err_meg = json.loads(form.errors.as_json())
            message = list()
            err_dict = {'usernamesignup': '用户名', 'emailsignup': '邮箱',
                        'passwordsignup': '密码','passwordsignup_confirm': '确认密码',}
            for key in err_meg:
                for err in err_meg[key]:
                    message.append("%s: %s" % (err_dict[key], err["message"]))
            return HttpResponse(json.dumps({"success": False, 'message': message}))

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/users/login/")