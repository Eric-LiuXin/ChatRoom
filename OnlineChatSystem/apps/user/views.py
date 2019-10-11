from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import LoginForm, SignUpForm
import json
import os
from django.conf import settings
from .models import User
from django.contrib.auth.hashers import make_password
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")


def user_login(request):
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

                logger.info("%s 登录"%user.username)

                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, 'msg': ["用户名密码验证失败！",]})
        else:
            err_meg = json.loads(form.errors.as_json())
            message = list()
            err_dict = {'username': '用户名', 'password': '密码',}
            for key in err_meg:
                for err in err_meg[key]:
                    message.append("%s: %s" % (err_dict[key], err["message"]))
            return JsonResponse({"success": False, 'msg': message})
    elif request.method == 'GET':
        return render(request, 'users/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                return JsonResponse({'success': False, 'msg': '两次输入密码不一致'})
            elif User.objects.filter(username=username):
                return JsonResponse({'success': False, 'msg': '该账号已存在'})
            elif User.objects.filter(nickname=nickname):
                return JsonResponse({'success': False, 'msg': '该昵称已被注册'})

            try:
                user = User(
                    username = username,
                    nickname=nickname,
                    password=make_password(password),
                    avatar = os.path.join('avatar', 'default_avatar.jpg')
                )
                user.save()
            except Exception as e:
                return JsonResponse({'success':False, 'msg':'服务器创建用户失败', 'detail':repr(e)})

            return JsonResponse({'success': True, 'msg': '用户创建成功，请登录'})
        else:
            err_meg = json.loads(form.errors.as_json())
            message = list()
            err_dict = {'username': '用户名', 'nickname': '昵称',
                        'password': '密码','confirm_password': '确认密码',}
            for key in err_meg:
                for err in err_meg[key]:
                    message.append("%s: %s" % (err_dict[key], err["message"]))
            return JsonResponse({"success": False, 'msg': message})
    else:
        return render(request, 'users/signup.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/user/login/")

def upload_avatar(request):
    try:
        user = request.user
        file_obj = request.FILES.get('croppedImage')
        save_path = os.path.join('avatar', '%s_avatar.jpg' % (user.nickname))
        file_path = os.path.join(settings.MEDIA_ROOT, 'avatar', '%s_avatar.jpg' % (user.nickname))
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        user.avatar = save_path
        user.save()

        return JsonResponse({"success": True, 'avatar_url': os.path.join('/media', save_path)})
    except Exception as e:
        return JsonResponse({"success": False, 'message': "上传失败！", "detail":repr(e)})