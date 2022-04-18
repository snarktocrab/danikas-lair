from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find/<username>/<alias>/code', views.code, name='Macro')
]
