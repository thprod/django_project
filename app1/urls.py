from django.urls import path
from app1 import views

urlpatterns = [
    path('app1.html', views.app1, name='app1.html'),
    path('', views.app1, name='app1.html'),
    path('about.html', views.about, name='About'),
]
