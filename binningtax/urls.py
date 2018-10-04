from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('tax/', views.tax, name='tax'),
    path('immigration/', views.immigration, name='immigration'),
    path('indian/', views.indian, name='indian'),
    path('contact', views.contact, name='contact'),
]
