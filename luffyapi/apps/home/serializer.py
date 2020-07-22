from rest_framework.serializers import Serializer,ModelSerializer
from . import models

class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('img','name','link')
