from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

# Create your views here.


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = ( IsAuthorOrReadOnly , )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):  # viewset config
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
