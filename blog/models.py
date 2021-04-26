from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args= [str(self.id)])    

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    

    def __str__(self):
        return self.user.username