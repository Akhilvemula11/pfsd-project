from django.urls import path

from . import views
from .views import login

app_name = 'erp'

urlpatterns = [
    path('', views.home, name='base'),

    # '''path('login/', views.login, name='login'),'''
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('first/', views.first, name='first'),

    path('sigin/', views.sigin, name='sigin'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('chat/', views.chat, name='chat'),
    path('doc/', views.doc, name='doc'),
    path('prof/', views.prof, name='prof'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
]