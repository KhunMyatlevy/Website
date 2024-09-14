from django.db import models

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Display a snippet of the content

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    # Optionally, you can add additional fields like caption or alt text

class PostVideo(models.Model):
    post = models.ForeignKey(Post, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_videos/')  # For video uploads
    # Alternatively, use URLField for embedding video URLs:
    # video_url = models.URLField(blank=True, null=True)
