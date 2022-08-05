from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import uuid

def uuid_default():
    return uuid.uuid4()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents/'+'user_{0}/{1}/{2}'.format(instance.user.username, instance.uuid, filename)


class SessionInstance(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid_default, editable=False)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='session_instances', on_delete=models.CASCADE)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    session_instance = models.ForeignKey(SessionInstance, on_delete=models.CASCADE, related_name='files')
