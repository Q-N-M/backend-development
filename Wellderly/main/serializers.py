from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'gender', 'username', 'password')


        def create(self, validated_data):
            return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label = 'username',
        max_length = 100,
        write_only = True
    )

    password = serializers.CharField(
        label = 'password',
        max_length = 256,
        trim_whitespace = False,
        write_only = True
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Username and password are required')
        else:
            raise serializers.ValidationError('Username and password are required')
        
        data["user"] = user
        return data
