from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import Post, Image, Service, Project, TeamMember, Client, About, ContactMessage, PostDetail


# ============================
# تصاویر پست‌ها
# ============================
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image_field:
            return format_html('<img src="{}" style="width: 80px; height:auto; border-radius:4px;" />',
                               obj.image_field.url)
        return "-"

    preview.short_description = _('پیش‌نمایش')


# ============================
# پست‌ها
# ============================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publish', 'image_count')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'description', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('-publish',)
    inlines = [ImageInline]

    def image_count(self, obj):
        return obj.images.count()

    image_count.short_description = _('تعداد تصویر')

    # فارسی سازی ستون‌ها
    title = _('عنوان')
    author = _('نویسنده')
    status = _('وضعیت')
    publish = _('تاریخ انتشار')


# ============================
# جزییات پست ها
# ============================

@admin.register(PostDetail)
class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('post', 'sku', 'price', 'stock', 'condition', 'is_available', 'image_count')
    list_filter = ('condition', 'is_available', 'created')
    search_fields = ('post__title', 'sku')
    ordering = ('-created',)
    inlines = [ImageInline]

    def image_count(self, obj):
        return obj.images.count()

    image_count.short_description = _('تعداد تصویر')


# ============================
# خدمات
# ============================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    # فارسی سازی ستون‌ها
    title = _('عنوان')
    is_active = _('فعال؟')
    created_at = _('تاریخ ایجاد')


# ============================
# پروژه‌ها
# ============================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_visible', 'preview_image')
    list_filter = ('category', 'is_visible', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height:auto; border-radius:4px;" />', obj.image.url)
        return "-"

    preview_image.short_description = _('پیش‌نمایش')


# ============================
# اعضای تیم
# ============================
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'preview_photo', 'joined_at')
    search_fields = ('name', 'role')
    ordering = ('-joined_at',)

    def preview_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width:50px; height:auto; border-radius:50%;" />', obj.photo.url)
        return "-"

    preview_photo.short_description = _('عکس')


# ============================
# مشتریان / برندها
# ============================
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'preview_logo', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

    def preview_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width:50px; height:auto;" />', obj.logo.url)
        return "-"

    preview_logo.short_description = _('لوگو')


# ============================
# درباره ما
# ============================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'updated_at')
    search_fields = ('heading', 'content')
    ordering = ('-updated_at',)


# ============================
# پیام‌های تماس
# ============================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'short_message', 'sent_at_formatted')
    readonly_fields = ('full_name', 'email', 'subject', 'message', 'sent_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sent_at',)
    ordering = ('-sent_at',)

    def short_message(self, obj):
        return (obj.message[:50] + '...') if len(obj.message) > 50 else obj.message

    short_message.short_description = _('خلاصه پیام')

    def full_name(self, obj):
        return obj.name

    full_name.short_description = _('نام و نام خانوادگی')

    def email(self, obj):
        return obj.email

    email.short_description = _('ایمیل')

    def subject(self, obj):
        return obj.subject

    subject.short_description = _('موضوع')

    def sent_at_formatted(self, obj):
        return obj.sent_at.strftime('%Y/%m/%d - %H:%M')

    sent_at_formatted.short_description = _('تاریخ ارسال')
