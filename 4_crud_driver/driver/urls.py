from django.urls import path

from driver import views

urlpatterns = [
    path('', views.drivers, name='all_drivers'),
    path('add/', views.add_driver, name='add_driver'),

]
