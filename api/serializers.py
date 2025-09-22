from rest_framework import serializers
from blog.models import *
import re


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '--all--'
#
#
# class PostDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostDetail
#         fields = '__all__'
#         extra_kwargs = {
#             'created': {'read_only': True},
#             'updated': {'read_only': True},
#         }
#
#     def validate_price(self, value):
#         if value < 0:
#             raise serializers.ValidationError("قیمت نمی‌تواند منفی باشد.")
#         return value
#
#     def validate_stock(self, value):
#         if value < 0:
#             raise serializers.ValidationError("موجودی نمی‌تواند منفی باشد.")
#         return value

class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'url']

    def get_url(self, obj):
        if not obj.image_field:
            return None
        request = self.context.get('request')
        img_url = obj.image_field.url
        if request:
            return request.build_absolute_uri(img_url)
        return img_url


class PostDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='post.images', many=True, read_only=True)  # عکس‌های پست مادر
    post = serializers.PrimaryKeyRelatedField(read_only=True)

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


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)  # عکس‌های خود پست
    details = PostDetailSerializer(read_only=True)  # چون related_name="details" در PostDetail دارید
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'description',
            'author', 'publish', 'created', 'updated',
            'status', 'images', 'details'
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
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
