from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from core.user.models import User

# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(AbstractSerializer):
    # id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    # created = serializers.DateTimeField(read_only=True)
    # updated = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
        'last_name', 'bio', 'avatar', 'email',
        'is_active', 'created', 'updated']
        read_only_field = ['is_active']