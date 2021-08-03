
"""cropperapi model serializers (define model fields accessible in API)."""
from logging import getLogger
import urllib.parse

from rest_framework import serializers

from .models import URL

logger = getLogger(__name__)


class URLSerializer(serializers.ModelSerializer):
    # Custom attribute
    shortened_url = serializers.SerializerMethodField()
    class Meta:
        model = URL
        fields = [
            'url',
            'shortened_url',
            'mins_since_created',
            #'url_hash',
            #'created',
        ]
    def get_shortened_url(self, obj):
        """Combine server hostname with url_hash if available."""
        uri = ''
        request = self.context.get('request')
        if request and hasattr(request, 'build_absolute_uri'):
            try:
                uri = request.build_absolute_uri()
            except Exception as e:
                logger.error(f'Failed to get host: {e}')
        return urllib.parse.urljoin(uri, obj.url_hash) if uri else obj.url_hash
