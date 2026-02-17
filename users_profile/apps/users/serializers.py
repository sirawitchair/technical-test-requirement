from rest_framework.serializers import ModelSerializer
from .models import User, UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'