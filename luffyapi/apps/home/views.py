from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.response import Response
from . import serializer
from django.conf import settings

class Home(APIView):
    def get(self,request):
        print(request.data)
        return Response("ok")

class Banner(ListAPIView,GenericAPIView):
    queryset = models.Banner.objects.filter(is_delete=False,is_display=True).order_by('display_order')[:settings.BANNER_COUNTER]
    serializer_class = serializer.BannerModelSerializer
