from django.contrib import admin
from .models import Post, PostImage, PostVideo

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1  # Number of empty forms to display initially

class PostVideoInline(admin.TabularInline):
    model = PostVideo  # Inline for videos
    extra = 1  # Number of empty video forms to display initially

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, PostVideoInline]  # Include both image and video inlines
    list_display = ('created_at',)
    search_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)  # Optional: Register PostImage if you want a separate admin page for images
admin.site.register(PostVideo)  # Optional: Register PostVideo if you want a separate admin page for videos
