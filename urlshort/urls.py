from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('go',views.makeShortUrl),
    path('<str:shorturl>',views.redirectURL)
]