from django.shortcuts import render
from .forms import ChatInputForm
from user.models import User
from django.db.models import Q

def chat(request):
    return render(request, 'room/index.html')


def self_chat_room(request):
    friend_list = User.objects.filter(~Q(id=request.user.id))
    chat_input_form  = ChatInputForm(
        initial={'Description': u'测试'}
    )

    return render(request, 'room/self_chat_room.html', locals())