from django.contrib.auth.models import User
from user_info.models import Info
from user_info.serializers import InfoSerializer
from rest_framework import serializers
from django.utils.timezone import now
from rest_framework.renderers import JSONRenderer

class UserSerializer(serializers.ModelSerializer):
    imageUrl = serializers.SerializerMethodField('get_imageUrl')
    class Meta:
        model = User
        fields = '__all__' 
        # fields = ['id', 'username', 'email','first_name','last_name', 'is_superuser','get_days_since_joined' ]

    def get_imageUrl(self, obj):
        try:
            info = Info.objects.get(user_id=obj.id)
            # serializer1 = InfoSerializer(info)
            image = getattr(info, 'image')
            if image and hasattr(image, 'url'):
                return image.url
            return ""
        except Info.DoesNotExist:
           
            return None
       
        