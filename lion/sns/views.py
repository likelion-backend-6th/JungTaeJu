from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .serializers import UserSerializer

# def user_list(request):
#     # users = User.objects.all()
#     # return render(request, 'blog/users.html', {'users': users})
#     queryset = 
@extend_schema(tags=["User"])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer