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
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'url']

    def get_url(self, obj):
        """
        اگر اسم فیلد فایل/عکس شما در مدل Image چیزی به جز `image_field` است،
        اینجا آن اسم را جایگزین کنید (مثلاً `image` یا `file`).
        اینجا کمی محافظ‌کارانه بررسی می‌کنیم چند نام ممکن را.
        """
        # سعی می‌کنیم نام‌های معمول را پشتیبانی کنیم؛ اگر مدل شما نام دیگری دارد، تغییر بده.
        image_field = getattr(obj, 'image_field', None) or getattr(obj, 'image', None) or getattr(obj, 'file', None)
        if not image_field:
            return None

        try:
            img_url = image_field.url
        except Exception:
            return None

        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(img_url)
        return img_url

    def get_title(self, obj):
        # عنوان را از پست مادر می‌گیریم
        return getattr(obj.post, 'title', None)

    def get_description(self, obj):
        # توضیحات را از پست مادر می‌گیریم
        return getattr(obj.post, 'description', None)


class PostDetailSerializer(serializers.ModelSerializer):
    # تصاویر پست مادر (Post) — source='post.images' چون PostDetail دارای FK به Post است
    images = ImageSerializer(source='post.images', many=True, read_only=True)
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
    # چون هر پست فقط یک detail دارد (OneToOneField)، many=False می‌گذاریم:
    details = PostDetailSerializer(read_only=True)
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

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['phone', 'address', 'email', 'instagram', 'telegram']


class AboutSerializer(serializers.ModelSerializer):
    contact_infos = ContactInfoSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['id', 'heading', 'content', 'image', 'updated_at', 'contact_infos']


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
