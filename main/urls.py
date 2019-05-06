from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('addMenu/', views.addMenu, name='addMenu')
]