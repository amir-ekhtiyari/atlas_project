from django.urls import path
from . import views
from .views import ContactMessageAPIView

app_name = 'api'

urlpatterns = [
    path('posts/', views.PostListAPIView.as_view(), name='post-list'),
    # لیست + ایجاد
    path('postdetails/', views.PostDetailListCreateAPIView.as_view(), name='postdetail-list-create'),

    # دریافت/ویرایش/حذف با id (پارامتر: pk)
    path('postdetails/<int:pk>/', views.PostDetailRetrieveUpdateDestroyAPIView.as_view(), name='postdetail-rud'),

    # (اختیاری) دریافت با slug پست (پارامتر: post_slug)
    path('postdetails/by-post/<slug:post_slug>/', views.PostDetailByPostSlugAPIView.as_view(), name='postdetail-by-post-slug'),
    path('services/', views.ServiceListAPIView.as_view(), name='service-list'),
    path('projects/', views.ProjectListAPIView.as_view(), name='project-list'),
    path('team/', views.TeamListAPIView.as_view(), name='team-list'),
    path('clients/', views.ClientListAPIView.as_view(), name='client-list'),
    path('about/', views.AboutAPIView.as_view(), name='about'),
    path('contact/', ContactMessageAPIView.as_view(), name='contact-message-api'),
]
