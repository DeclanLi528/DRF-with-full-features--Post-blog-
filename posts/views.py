from .serializers import Postserializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Post
# Create your views here.


#ListCreateAPIView 支持GET和POST
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer

#RetrieveUpdateDestroyAPIView 支持GET PUT/PATCH DELETE
#完整的CRUD create read update delete
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = Postserializer
