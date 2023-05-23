from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'category', 'creator', 'creation_time', 'content', "image", "creator_username", "creator_image")
        read_only_fields = ['creation_time']
        creator = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
        category = serializers.ModelField(models.Category, read_only=True)

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.content = validated_data.get('content', instance.content)
    #     try:
    #         instance.image = validated_data.get('image', instance.content)
    #     except:
    #         pass
    #     instance.save()
    #     return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('user', 'image')
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(UserProfileSerializer, self).create(validated_data)
