from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name = 'panel'),
    path('displayForm', views.displayForm, name = 'displayForm'),
    path('insertData', views.insertData, name = 'insertData'),
    path('deleteData/<int:pk>', views.deleteData, name = 'deleteData'),
    path('editData/<int:pk>', views.editData, name = 'editData'),

] 
