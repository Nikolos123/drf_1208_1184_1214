from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework.renderers import JSONRenderer
from  rest_framework.viewsets import ModelViewSet
from .models import Author,Book,Biography
from .serialiazers import AuthorModelSerializer, BookSerializer, BiographyModelSerializer, AuthorModelSerializerBase


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class AuthorModelViewSet(ModelViewSet):

    queryset = Author.objects.all()
    # serializer_class = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AuthorModelSerializerBase
        return AuthorModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

