from blog.models import *
from .serializers import *
from rest_framework import generics,  permissions
from rest_framework.parsers import MultiPartParser, FormParser



class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.active()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.visible()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class TeamListAPIView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.AllowAny]


class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]


class AboutAPIView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return self.queryset.first()  # فقط یک about داریم


class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

