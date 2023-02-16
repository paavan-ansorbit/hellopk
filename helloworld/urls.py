from django.urls import path
from . import views

urlpatterns = [
   path('create', views.create_user, name='create_user'),
   path('', views.get_user, name='get_user'),    
   path('delete/<str:id>', views.delete_user, name='delete_user'),
   path('update/<str:id>', views.update_user, name='update_user'),
   path('<str:id>', views.get_user_by_id, name='get_user_by_id'),
   path('deleteall', views.delete_all, name='delete_all'),
] 