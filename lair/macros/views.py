from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.template import loader
from .models import Macro


# Create your views here.
def index(request):
    macros = Macro.objects.filter(public=True).order_by('alias')
    #mac_list = [{
    #    'owner': m.owner.username,  
    #    'alias': m.alias,
    #    'id':    m.id,
    #    } for m in macros]
    context = { 'public_macros_list': macros }
    return render(request, 'index.html', context)
    #return HttpResponse('\n'.join([f"{m.owner}\t{m.alias}\t'{m.code}'" for m in macros]))


def code(request, username, alias):
    user = get_user_model().objects.get(username=username)
    macro = get_object_or_404(Macro, owner=user, alias=alias)
    return HttpResponse(macro.code)

def code(request, pk):
    macro = get_object_or_404(Macro, id=pk)
    return HttpResponse(macro.code)
