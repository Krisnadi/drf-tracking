from .base_models import BaseAPIRequestLog
from django.db import models


class APIRequestLog(BaseAPIRequestLog):
    country = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
