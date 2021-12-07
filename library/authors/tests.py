from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import Author, Biography


# Create your tests here.

class TestAuthorViewSet(TestCase):
    # url = '/api/authors/'

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'

        self.data ={'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}
        self.data_put = {'first_name': 'Николай', 'last_name': 'Нагорный', 'birthday_year': 1990}
        self.url = '/api/authors/'
        self.admin = User.objects.create_superuser(self.name,'admin@amail.ru',self.password)

    def test_get_list(self):
        # создаем объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.get(self.url)
        # указываем как тип запроса будет переда в AuthorModelViewSet
        view = AuthorModelViewSet.as_view({'get': 'list'})
        # передаем во вью и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        # создаем объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.post(self.url,self.data,format='json' )
        # указываем как тип запроса будет переда в AuthorModelViewSet
        view = AuthorModelViewSet.as_view({'post': 'create'})
        # передаем во вью и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        # создаем объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.post(self.url, self.data, format='json')

        #авторизоваться
        force_authenticate(request,self.admin)
        # указываем как тип запроса будет переда в AuthorModelViewSet
        view = AuthorModelViewSet.as_view({'post': 'create'})
        # передаем во вью и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        #создаем объект класса APIClient
        client = APIClient()
        #создать автора через ORM для проверки детализации
        author = Author.objects.create(**self.data)
        #сделать запрос
        response = client.get(f'{self.url}{author.id}/')
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guest(self):
        #создаем объект класса APIClient
        client = APIClient()
        #создать автора через ORM для проверки обновления
        author = Author.objects.create(**self.data)
        #сделать запрос
        response = client.put(f'{self.url}{author.id}/',self.data_put)
        #проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_admin(self):
        #создаем объект класса APIClient
        client = APIClient()
        #создать автора через ORM для проверки обновления
        author = Author.objects.create(**self.data)
        #авторизоваться
        client.login(username=self.name,password=self.password)
        #сделать запрос
        response = client.put(f'{self.url}{author.id}/',self.data_put)
        #проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #получаем автора
        author_update = Author.objects.get(id=author.id)
        #сделать проверку
        self.assertEqual(author_update.first_name,'Николай')
        self.assertEqual(author_update.last_name,'Нагорный')
        self.assertEqual(author_update.birthday_year,1990)
        client.logout()

    def tearDown(self) -> None:
        pass

class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response,2)

class TestBiographyViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'

        self.data = {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}
        self.data_put = {'first_name': 'Николай', 'last_name': 'Нагорный', 'birthday_year': 1990}
        self.url = '/api/biography/'
        self.admin = User.objects.create_superuser(self.name, 'admin@amail.ru', self.password)

    def test_get_list(self):
        #делаем запрос
        response = self.client.get(self.url)
        #проверяем ответ
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_edit_admin(self):
        #создать автора через ORM для связи с биографией
        author = Author.objects.create(**self.data)
        #созлать биографию
        bio = Biography.objects.create(text='test',author=author)
        #авторизоваться
        self.client.login(username=self.name,password=self.password)
        #запрос
        response = self.client.put(f'{self.url}{bio.id}/',
                                   {'text': 'Biography','author': bio.author.id})
        #проверяем ответ
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        #получаем биографию
        biog = Biography.objects.get(id=bio.id)
        #сделать проверку
        self.assertEqual(biog.text,'Biography')
        #разлогинимся
        self.client.logout()

    def test_edit_mixer(self):
        # # создать автора через ORM для связи с биографией
        # author = Author.objects.create(**self.data)
        # # созлать биографию
        bio = mixer.blend(Biography)
        # авторизоваться
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/',
                                   {'text': 'Biography', 'author': bio.author.id})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем биографию
        biog = Biography.objects.get(id=bio.id)
        # сделать проверку
        self.assertEqual(biog.text, 'Biography')
        # разлогинимся
        self.client.logout()

    def test_edit_mixer_text(self):
        # # создать автора через ORM для связи с биографией
        # author = Author.objects.create(**self.data)
        # # созлать биографию
        bio = mixer.blend(Biography,text='Вася')
        # авторизоваться
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/',
                                   {'text': 'Biography', 'author': bio.author.id})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем биографию
        biog = Biography.objects.get(id=bio.id)
        # сделать проверку
        self.assertEqual(biog.text, 'Biography')
        # разлогинимся
        self.client.logout()



