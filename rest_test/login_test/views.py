from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

import json
from .models import User
from django.views import View
from django.http import JsonResponse



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'pwd', 'name', 'birth', 'email', 'phone_num', 'addr', 'rcmd_id', 'category')

def index_page(request):
    return render(request, './index.html')

def register_page(request):
    return render(request, './register.html')


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        id = serializer.data.get('id')
        pwd = serializer.data.get('pwd')
        name = serializer.data.get('name')
        birth = serializer.data.get('birth')
        email = serializer.data.get('email')
        phone_num = serializer.data.get('phone_num')
        addr = serializer.data.get('addr')
        rcmd_id = serializer.data.get('rcmd_id')
        category = serializer.data.get('category')
        return Response(serializer.data, status=201)  # Successful post
    else:
        return Response(serializer.errors, status=400)  # Invalid data


# 데이터 통신 확인
@api_view(['GET'])
def check_data(request):
    # serializer = UserSerializer(data=request.data)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def login(request):
    pass

@api_view(['GET', 'POST'])
def logout(request):
    pass

@api_view(['GET', 'POST'])
def modify(reqeust):
    pass