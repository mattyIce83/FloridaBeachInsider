import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Image
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


def create_image(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["caption"] = "caption"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    return Image.objects.create(**defaults)


class ImageViewTest(unittest.TestCase):
    '''
    Tests for Image
    '''
    def setUp(self):
        self.client = Client()

    def test_list_image(self):
        url = reverse('images_image_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_image(self):
        url = reverse('images_image_create')
        data = {
            "title": "title",
            "caption": "caption",
            "image": "image",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_image(self):
        image = create_image()
        url = reverse('images_image_detail', args=[image.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_image(self):
        image = create_image()
        data = {
            "title": "title",
            "caption": "caption",
            "image": "image",
        }
        url = reverse('images_image_update', args=[image.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)