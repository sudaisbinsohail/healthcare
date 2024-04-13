from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only':True}
        }


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def create(self , validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
class LoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.user_name', read_only=True)
    fullname = serializers.CharField(source='user.full_name', read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")
        user = User.objects.filter(email=email).first()
        if not user.check_password(password):
              raise serializers.ValidationError("Please provide correct email and password.")
        data['user'] = user
        return data

