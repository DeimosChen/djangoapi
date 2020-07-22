from django.shortcuts import render
import re
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from . import models
from luffyapi.utils.response import APIResponse
from . import serializer

class LoginView(ViewSet):
    @action(methods=['POST'],detail=False)
    def login(self,request,*args,**kwargs):
        ser = serializer.UserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            login_type = ser.context['login_type']
            username = ser.context['username']
            return APIResponse(token=token,login_type=login_type,username=username)
        else:
            return APIResponse(code=0,msg=ser.errors)

    @action(methods=['POST'], detail=False)
    def check_phone(self,request,*args,**kwargs):
        phone = request.data.get('phone')
        if not re.match('^1[3-9][0-9]{9}$',phone):
            return APIResponse(code=0,msg='手机号格式错误')
        try:
            models.User.objects.get(phone=phone)
            return APIResponse(msg='True')
        except:
            return APIResponse(code=0,msg='手机号不存在')


