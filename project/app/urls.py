from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.superadmin),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('home/',views.home,name='home'),
    
]