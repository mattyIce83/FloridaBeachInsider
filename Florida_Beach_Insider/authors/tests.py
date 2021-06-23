import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_author(**kwargs):
    defaults = {}
    defaults["first_name"] = "first_name"
    defaults["last_name"] = "last_name"
    defaults["slug_name"] = "slug_name"
    defaults["active"] = "active"
    defaults["title"] = "title"
    defaults["bio"] = "bio"
    defaults["photo"] = "photo"
    defaults["email"] = "email"
    defaults["facebook"] = "facebook"
    defaults["twitter"] = "twitter"
    defaults["instagram"] = "instagram"
    defaults.update(**kwargs)
    return Author.objects.create(**defaults)


class AuthorViewTest(unittest.TestCase):
    '''
    Tests for Author
    '''
    def setUp(self):
        self.client = Client()

    def test_list_author(self):
        url = reverse('authors_author_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_authors(self):
        url = reverse('authors_author_create')
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "slug_name": "slug_name",
            "active": "active",
            "title": "title",
            "bio": "bio",
            "photo": "photo",
            "email": "email",
            "facebook": "facebook",
            "twitter": "twitter",
            "instagram": "instagram",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_author(self):
        author = create_author()
        url = reverse('authors_author_detail', args=[author.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_author(self):
        author = create_author()
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "slug_name": "slug_name",
            "active": "active",
            "title": "title",
            "bio": "bio",
            "photo": "photo",
            "email": "email",
            "facebook": "facebook",
            "twitter": "twitter",
            "instagram": "instagram",
        }
        url = reverse('authors_author_update', args=[author.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


