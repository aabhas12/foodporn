from rest_framework import serializers
from user.models import Users
import datetime




class UsergetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Users
        fields = "__all__"

class UsersetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Users
        fields = ('firstname','email','username','avatar','social_media_id')

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        return user


