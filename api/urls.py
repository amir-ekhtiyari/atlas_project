from django.urls import path
from . import views
from .views import ContactMessageAPIView

app_name = 'api'

urlpatterns = [
    path('posts/', views.PostListAPIView.as_view(), name='post-list'),
    path('postdetails/', views.PostDetailListAPIView.as_view(), name='postdetail-list'),
    path('services/', views.ServiceListAPIView.as_view(), name='service-list'),
    path('projects/', views.ProjectListAPIView.as_view(), name='project-list'),
    path('team/', views.TeamListAPIView.as_view(), name='team-list'),
    path('clients/', views.ClientListAPIView.as_view(), name='client-list'),
    path('about/', views.AboutAPIView.as_view(), name='about'),
    path('contact/', ContactMessageAPIView.as_view(), name='contact-message-api'),
]
