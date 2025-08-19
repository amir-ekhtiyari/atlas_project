from blog.models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostDetailListAPIView(generics.ListAPIView):
    queryset = PostDetail.objects.all()
    serializer_class = PostDetailSerializer
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


class ContactMessageAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'پیام با موفقیت ارسال شد.'}, status=201)
        return Response(serializer.errors, status=400)
