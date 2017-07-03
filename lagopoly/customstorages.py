from django.conf import settings
from decouple import config
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION
    host = "s3.{}.amazonaws.com".format(config('AWS_REGION'))

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
    host = "s3.{}.amazonaws.com".format(config('AWS_REGION'))