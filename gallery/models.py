from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')  # Store the image in 'images/' folder
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_images', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_images', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
