import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Filter
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


def create_filter(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["active"] = "active"
    defaults.update(**kwargs)
    return Filter.objects.create(**defaults)


class FilterViewTest(unittest.TestCase):
    '''
    Tests for Filter
    '''
    def setUp(self):
        self.client = Client()

    def test_list_filter(self):
        url = reverse('filters_filter_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_filter(self):
        url = reverse('filters_filter_create')
        data = {
            "name": "name",
            "active": "active",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_filter(self):
        filter = create_filter()
        url = reverse('filters_filter_detail', args=[filter.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_filter(self):
        filter = create_filter()
        data = {
            "name": "name",
            "active": "active",
        }
        url = reverse('filters_filter_update', args=[filter.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


