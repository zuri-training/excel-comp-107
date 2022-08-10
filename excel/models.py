from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents/'+'user_{0}/{1}/{2}'.format(instance.post.user.username, instance.post.id, filename)


class Post(models.Model):
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self) -> str:
		  return str(self.id) + ": " + str(self.user.username)


class Document(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='documents', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.uploaded_at)
