from django.test import TestCase

from .factories import URLFactory
from ..models import URL
from ..serializers import URLSerializer


class URLSerializerTestCase(TestCase):
    def setUp(self):
        self.expected_fields = set(['url', 'shortened_url', 'mins_since_created',])
        self.url = URLFactory.create()
        self.serializer = URLSerializer(self.url)

    def test_contains_expected_fields(self):
        self.assertEqual(set(self.serializer.data.keys()), self.expected_fields)

    def test_get_shortened_url(self):
        # Result will be just url_hash value without a request context (this case)
        # or server URI + url_hash (Ex. http://127.0.0.1:8000/v1/abc123)
        self.assertEqual(self.serializer.data['shortened_url'], self.url.url_hash)

    def test_create_serializer_with_valid_url(self):
        s = URLSerializer(data={'url': 'https://github.com'})
        self.assertTrue(s.is_valid())
        self.assertTrue('url' not in s.errors)

    def test_create_serializer_with_invalid_url(self):
        s = URLSerializer(data={'url': 'heyday'})
        self.assertFalse(s.is_valid())
        self.assertTrue('url' in s.errors)
