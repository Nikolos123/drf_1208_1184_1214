from rest_framework.renderers import JSONRenderer
from  rest_framework.viewsets import ModelViewSet
from .models import Author,Book,Biography
from .serialiazers import AuthorModelSerializer,BookModelSerializer,BiographyModelSerializer

class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

