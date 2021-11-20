from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from .models import Author,Biography,Book

class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        # fields = ('first_name','last_name')
        # exclude =('birthday_year')

class BiographyModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'

class BookModelSerializer(ModelSerializer):

    # author = AuthorModelSerializer(many=True)
    author = StringRelatedField(many=True)
    # StringRelatedField

    # def create(self, validated_data):
    #     pass
    class Meta:
        model = Book
        fields = '__all__'