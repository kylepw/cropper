from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from ..models import URL
from ..utils import generate_hash


class URLTestCase(TestCase):
    def setUp(self):
        self.url = URL.objects.create(
            url='https://en.wikipedia.org/wiki/Year_2000_problem',
        )

    def test_mins_since_created(self):
        self.url.created = timezone.now() - timedelta(minutes=10)
        self.assertEqual(self.url.mins_since_created, 10)

    def test_str(self):
        self.assertEqual(str(self.url), f'{self.url.url} ({self.url.url_hash})')

    def test_alid_url_hash_saved_from_generate_hash(self):
        sample_hash = generate_hash(URL)
        self.assertEqual(len(self.url.url_hash), len(sample_hash))
        self.assertTrue(self.url.url_hash.isalnum())
