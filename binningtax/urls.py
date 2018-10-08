from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('tax-services/', views.tax, name='tax-services'),
    path('immigration-help/', views.immigration, name='immigration-help'),
    path('indian-services/', views.indian, name='indian-services'),
    path('contact-us/', views.contact, name='contact-us'),
]
