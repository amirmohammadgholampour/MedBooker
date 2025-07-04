from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from apps.main_models.user_models import User 
from apps.main_serializers.auth_serializer import UserSerializer 

@api_view(["GET"]) 
def get_user_list(request, *args, **kwargs):
    queryset = User.objects.all() 
    serializer = UserSerializer(queryset, many=True) 
    return Response(serializer.data) 