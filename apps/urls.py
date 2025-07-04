from django.urls import path 
from apps.main_views.auth_view import get_user_list 

urlpatterns = [
    path("api/users/", get_user_list)
]