from rest_framework import serializers
from account.models import Information
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


# class UserRegistrationSerializer(serializers.Serializer):
#     username = serializers.CharField(required = True)
#     password = serializers.CharField(write_only = True, required = True)
#     token = serializers.CharField(read_only = True)

#     class Meta:
#         model = User
#         fields = ['username','email','password','token']

#     def create(self,validated_data):
#         username = validated_data.get('username')
#         email = validated_data.get('email')
#         user = User(
#             username = username,
#             email = email
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         # get or generate token 
#         token,created = Token.objects.get_or_create(user = user)

#         user.token = token.key
#         return user
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    token = serializers.CharField(read_only = True)

    class Meta:
        model = User
        fields = ['username','email','password','token']

    def create(self,validated_data):
        username = validated_data['username']
        email = validated_data['password']
        user = User(
            username = username,
            email = email
        )
        user.set_password(validated_data['password'])
        user.save()

        # get or generate token 
        token,created = Token.objects.get_or_create(user = user)

        user.token = token.key
        return user