from  rest_framework.viewsets import ModelViewSet
from .models import Author
from .serialiazers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
