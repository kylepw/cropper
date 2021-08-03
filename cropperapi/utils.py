"""cropperapi helper functions."""
import random
import string

from rest_framework import status
from rest_framework.views import exception_handler, Response

from .settings import URL_HASH_LENGTH


def custom_exception_handler(exc, context):
    """Steamline error responses with details placed in 'detail' of payload."""
    response = exception_handler(exc, context)

    if response is None:
        response = Response(
                {"detail": str(exc)},  status=status.HTTP_400_BAD_REQUEST
            )
    return response


def generate_hash(url_cls):
    """Generate unique, random alphanumeric hash for urls.
    
    Args:
        url_cls: URL model class.
    Returns:
        str: unique alphanumeric hash
    """
    def _generate_hash():
        valid_chars = string.ascii_lowercase + string.digits
        return "".join([random.choice(valid_chars) for _ in range(URL_HASH_LENGTH)])
    
    new_hash = _generate_hash()
    # Keep trying until we get a unique hash.
    while url_cls.objects.filter(url_hash=new_hash).exists():
        new_hash = _generate_hash()

    return new_hash


