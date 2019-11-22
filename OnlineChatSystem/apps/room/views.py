from django.shortcuts import render
from django.db.models import Q
from django.http import  JsonResponse
from django.template.loader import get_template
from user.models import User
from room.models import Room

def chat(request):
    return render(request, 'room/index.html')


def self_chat_room(request):
    friend_list = User.objects.filter(~Q(id=request.user.id))


    return render(request, 'room/self_chat_room.html', locals())

def join_room(request):
    friend_id = request.GET.get('friend_id')
    friend = User.objects.get(id=friend_id)

    user = request.user

    room, _ = Room.objects.get_or_create()

    template = get_template('room/chat_room.html', )
    html = template.render(locals())
    return JsonResponse({"success": True, 'html': html})

def user_card(request, user_id):
    user = User.objects.get(id=user_id)

    template = get_template('room/user_card.html', )
    html = template.render(locals())
    return JsonResponse({"success": True, 'html': html})