from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='postsImages', blank=True)

    @property
    def creator_username(self):
        return self.creator.username

    @property
    def creator_image(self):
        try:
            return self.creator.UserProfile.image
        except:
            return None

    def __str__(self):
        return self.content[0:10]+"|"+self.creator.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='usersProfileImages', blank=True)

    def __str__(self):
        return self.user.username
