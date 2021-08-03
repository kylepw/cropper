from django.test import TestCase

from .factories import URLFactory
from ..models import URL
from ..settings import URL_HASH_LENGTH
from ..utils import generate_hash


class GenerateHashTestCase(TestCase):
    def setUp(self):
        URLFactory.create_batch(10)
        self.hash_result = generate_hash(URL)

    def test_length(self):
        self.assertEqual(len(self.hash_result), URL_HASH_LENGTH)

    def test_isalnum(self):
        self.assertTrue(self.hash_result.isalnum())

    def test_hash_does_not_exist_in_db(self):
        self.assertFalse(URL.objects.filter(url_hash=self.hash_result).exists())
