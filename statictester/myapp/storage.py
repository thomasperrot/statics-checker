from django.contrib.staticfiles import storage
from storages.backends import gcloud


class ManifestGoogleCloudFilesStorage(
    storage.ManifestFilesMixin,
    gcloud.GoogleCloudStorage
):
    pass
