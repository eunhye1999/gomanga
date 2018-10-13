
from django.urls import path

from . import views

app_name = 'scdownload'

urlpatterns = [
    path('', views.index, name='index'),
    path('nhentai/', views.nhentai, name='nhentai'),
    path('nhentai/result/', views.nhentaiResult, name='nhentaiRe'),

    path('download/', views.downloadIMG, name='downloadIMG'),
]