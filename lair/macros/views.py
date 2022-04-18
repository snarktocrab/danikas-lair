from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Macro


# Create your views here.
def index(request):
    macros = Macro.objects.filter(public=True).order_by('alias')
    return HttpResponse('\n'.join([f"{m.owner}\t{m.alias}\t'{m.code}'" for m in macros]))


def code(request, username, alias):
    user = get_user_model().objects.get(username=username)
    macro = get_object_or_404(Macro, owner=user, alias=alias)
    return HttpResponse(macro.code)
