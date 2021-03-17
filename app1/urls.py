from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index, name='Index'),

    path('index.html', views.index, name='Index'),
    path('daniel.html', views.daniel, name='Daniel'),
    path('taylor.html', views.taylor, name='Taylor'),
    path('jesus.html', views.jesus, name='Jesus'),
    path('about.html', views.about, name='About'),
]
