"""cropperapi app views."""
from django.shortcuts import get_object_or_404, redirect
from rest_framework import mixins, status, viewsets

from .models import URL
from .serializers import URLSerializer


class URLViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def retrieve(self, request, pk=None):
        """ Retrieve objects by url_hash, not pk and redirect."""
        queryset = URL.objects.all()
        url = get_object_or_404(queryset, url_hash=pk)
        return redirect(url.url)