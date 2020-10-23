from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/', views.update, name='update'),
    path('longer/', views.longer, name='longer'),
    path('longer_update/', views.longerUpdate, name='longerUpdate'),
    path('graph/', views.graph, name='graph'),
]
