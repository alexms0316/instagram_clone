from django.db    import models
from users.models import User

class Posting(models.Model):
      content    = models.CharField(max_length=10000, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      user       = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='postings')

      class Meta:
          db_table = 'postings'

class Image(models.Model):
      image_url  = models.URLField(max_length=2000)
      image_post = models.ForeignKey('Posting', on_delete=models.CASCADE, related_name='images')

      class Meta:
          db_table = 'images'
