from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name = 'panel'),
    path('displayForm', views.displayForm, name = 'displayForm'),
    path('insertData', views.insertData, name = 'insertData'),
] 
