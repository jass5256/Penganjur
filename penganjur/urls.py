from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home_penganjur"),
    path('aktiviti/add/', views.addaktiviti, name="tambah_aktviti"),
    path('aktiviti/<int:pk>/delete/', views.deleteaktiviti, name="delete_aktviti"),
    path('aktiviti/<int:pk>/edit/', views.editaktiviti, name="edit_aktviti"),    
]
