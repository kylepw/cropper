from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import URLFactory
from ..models import URL


class URLViewSetTestCase(APITestCase):
    def setUp(self):
        URLFactory.create_batch(4)
        self.default_url = URL.objects.create(url='https://www.djangoproject.com')

    def test_list_count(self):
        url = reverse('url-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json['count'], 5)
        self.assertEqual(len(response_json['results']), 5)

    def test_list_pagination_works(self):
        PAGE_SIZE = int(settings.REST_FRAMEWORK['PAGE_SIZE'])
        URLFactory.create_batch(PAGE_SIZE * 2)

        url = reverse('url-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        # Should be as many results as PAGE_SIZE, but more in total count
        self.assertEqual(len(response_json['results']), PAGE_SIZE)
        self.assertGreater(response_json['count'], PAGE_SIZE)

    def test_list_new_url_in_results(self):
        new_url = URL(url='https://en.wikipedia.org/wiki/Year_2000_problem',)
        url = reverse('url-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertNotIn(new_url.url, [r['url'] for r in results])

        new_url.save()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertIn(new_url.url, [r['url'] for r in results])

    def test_detail_shortened_url_redirects(self):
        url = reverse('url-detail', args=[self.default_url.url_hash])
        response = self.client.get(url)
        self.assertRedirects(
            response, self.default_url.url, fetch_redirect_response=False
        )

    def test_create_valid_url(self):
        url = reverse('url-list')
        new_url = 'https://www.hodinkee.com/articles/how-the-left-wrist-became-the-right-wrist-for-watches-2'

        self.assertTrue(URL.objects.count(), 5)
        self.assertFalse(URL.objects.filter(url=new_url).exists())

        response = self.client.post(url, {'url': new_url})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()

        self.assertEqual(response_json['url'], new_url)
        self.assertTrue(URL.objects.count(), 6)
        self.assertTrue(URL.objects.filter(url=new_url).exists())

    def test_create_empty_url(self):
        url = reverse('url-list')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_url(self):
        url = reverse('url-list')
        invalid_url = 'jawnsjawnsjawns'

        response = self.client.post(url, {'url': invalid_url})
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Enter a valid URL.', response_json['url'])

    def test_create_url_that_already_exists(self):
        url = reverse('url-list')

        response = self.client.post(url, {'url': self.default_url.url})
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('url with this url already exists.', response_json['url'])
