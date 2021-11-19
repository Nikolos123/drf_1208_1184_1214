from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from .models import Author

class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'