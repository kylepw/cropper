"""Factories to populate test databases with data."""
from django.utils import timezone
import factory

from ..models import URL
from ..utils import generate_hash


class URLFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = URL

    # Need sequence to generate unique urls with create_batch()
    url = factory.Sequence(lambda n: f'https://www.example{n}.com')
    url_hash = generate_hash(URL)
    created = factory.Faker(
        "date_time_this_year",
        before_now=True,
        after_now=False,
        tzinfo=timezone.get_current_timezone(),
    )
