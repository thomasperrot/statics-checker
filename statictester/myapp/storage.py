from django.contrib.staticfiles import storage
from storages.backends import gcloud


class ManifestGoogleCloudFilesStorage(
    storage.ManifestFilesMixin,
    gcloud.GoogleCloudStorage
):
    max_post_process_passes = 5

    def get_default_settings(self):
        settings = super().get_default_settings()
        settings["bucket_name"] = "rh2-manifest"
        return settings
