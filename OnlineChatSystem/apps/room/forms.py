from  DjangoUeditor.forms import UEditorField
from django import forms
from datetime import datetime

def getImagePath(model_name):
    return "room/%s/image/%d/%d/"%(model_name, datetime.now().month, datetime.now().day)

class ChatInputForm(forms.Form):
    teletext = UEditorField('',initial="",width='auto', height='auto', imagePath=getImagePath('message'))
