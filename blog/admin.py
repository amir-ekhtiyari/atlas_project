from django.contrib import admin
from .models import *


# Register your models here.


# admin.site.register(Post) I prefer to use decorator not this foramt !

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    list_filter = ['status', 'publish', 'author']
    ordering = ['title', 'publish']
    search_fields = ['title', 'description']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['status']

# additional customise
# list_display_links = ['author']
# raw_id_fields = ['author']



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_visible', 'created_at')
    list_filter = ('category', 'is_visible', 'created_at')
    search_fields = ('title', 'description')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'joined_at')
    list_filter = ('joined_at',)
    search_fields = ('name', 'role', 'bio')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'updated_at')
    search_fields = ('heading', 'content')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read', 'sent_at')
    search_fields = ('name', 'email', 'subject', 'message')
