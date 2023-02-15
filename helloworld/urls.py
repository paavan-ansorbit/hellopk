from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ping', views.ping, name='ping'),
    path('version', views.version, name='version'),
    # path('create-user', views.create_user, name='create_user'),
    # path('get-user', views.get_user, name='get_user'),    
    # path('delete-user/<str:id>', views.delete_user, name='delete_user'),
    # path('update-user/<str:id>', views.update_user, name='update_user'),
    # path('get-user-by-id/<str:id>', views.get_user_by_id, name='get_user_by_id'),
    # path('delete-all', views.delete_all, name='delete_all'),
] 