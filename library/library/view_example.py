from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404

from authors.filters import BookFilter
from authors.models import Book
from authors.serialiazers import BookSerializer

# level 1 APIView
# class BookAPIView(APIView):
#     renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#
#     def get(self,request,format=None):
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         pass
# #
# @api_view(['GET','POST']) ##'POST'
# @renderer_classes([JSONRenderer,BrowsableAPIRenderer])
# def test(request):
      #if request.POST == 'POST'
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)
#         # return Response(serializer.data)
#         return Response({'test':1})###Дополнительный пример
      #elif request.GET == 'GET':

# level 2 Generic views
# class BookCreateAPIView(CreateAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
#
# class BookListAPIView(ListAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
# # #
# class BookRetrieveAPIView(RetrieveAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
# #
# class BookDestroyAPIView(DestroyAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
#
# class BookUpdateAPIView(UpdateAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

# level 3 ViewSets


# class BookViewSet(ViewSet):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#
#    def list(self,request):
#        book = Book.objects.all()
#        serializer_class = BookSerializer(book,many=True)
#        return Response(serializer_class.data)
#
#    def retrieve(self,request,pk=None):
#        book = get_object_or_404(Book, pk=pk)
#        serializer_class = BookSerializer(book)
#        return Response(serializer_class.data)
# #
#    @action(detail=True, methods=['get'])
#    def only(self, request, pk=None):
#        book = Book.objects.get(id=pk)
#        return Response({'book': book.name,'id':book.id})



# level 4 ModelViewSet (то что мы делали изначально самый просто способ)
# class BookViewSet(ModelViewSet):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer



# level 5 Custom ViewSet
#
# class BookCustomViewSet(ListModelMixin,CreateAPIView, DestroyModelMixin,RetrieveAPIView,UpdateAPIView,GenericViewSet):
#     queryset =  Book.objects.all()
#     serializer_class =  BookSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


# filter
# class BookQuerysetFilterViewSet(ModelViewSet):
#    serializer_class = BookSerializer
#    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#    queryset = Book.objects.all()
#
#    def get_queryset(self):
#        return Book.objects.filter(name__contains='bo')
#
#
# class BookListAPIView(ListAPIView):
#    serializer_class = BookSerializer
#
#    def get_queryset(self):
#        name = self.kwargs['name']
#        return Book.objects.filter(name__contains=name)
#
# class BookModelViewSet(ModelViewSet):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
#
#    def get_queryset(self):
#        name = self.request.query_params.get('name', '')
#        book = Book.objects.all()
#        if name:
#            book = book.filter(name__contains=name)
#        return book


#DjangoFilter

# class BookDjangoFilterViewSet(ModelViewSet):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
#    # filterset_fields = ['id','name']
#    filterset_class = BookFilter


# #PAGINATOR
class BookLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 3
# #
# #
class BookLimitOffsetPaginatonViewSet(ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   pagination_class = BookLimitOffsetPagination
       # BookLimitOffsetPagination