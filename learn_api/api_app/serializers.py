from rest_framework import serializers
from api_app.models import UserData, currency


class ApiAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['username', 'bio', 'website_link_1', 'website_link_2', 'website_link_3', 'profile_pic', 'currency']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Userdata.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.website_link_1 = validated_data.get('website_link_1', instance.website_link_1)
        instance.website_link_2 = validated_data.get('website_link_2', instance.website_link_2)
        instance.website_link_3 = validated_data.get('website_link_3', instance.website_link_3)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.save()
        return instance
