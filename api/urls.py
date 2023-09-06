from django.urls import path
from . import views


urlpatterns=[
    path('', views.getRoutes, name='routes'),
    path('links/', views.getLinks, name='links'),
    path('advantages/', views.getAdvantages, name='advantages')
]