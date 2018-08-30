from .models import Blog,Author,Entry
from .serializers import BlogSerializer,AuthorSerializer,EntrySerializer
from rest_framework.permissions import IsAuthenticated  # , IsAdminUser
from rest_framework import viewsets, mixins

class CURDViewSet(mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
	pass

class BlogListAPIView(CURDViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    #permission_classes = (IsAuthenticated,)

class AuthorListAPIView(CURDViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class EntryListAPIView(CURDViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer