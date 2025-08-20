from rest_framework import serializers
from blog.models import *
import re


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'status', 'slug']


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDetail
        fields = '__all__'
        extra_kwargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
        }

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("قیمت نمی‌تواند منفی باشد.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("موجودی نمی‌تواند منفی باشد.")
        return value


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', 'attachment', 'phone']

    def validate_phone(self, value):
        if not re.match(r'^09\d{9}$', value):
            raise serializers.ValidationError('شماره موبایل نامعتبر است.')
        return value
