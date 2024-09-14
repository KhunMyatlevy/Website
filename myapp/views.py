from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Home Page View
def home(request):
    return render(request, 'home.html')

# Post List View
from django.shortcuts import render
from .models import Post
from django.utils.text import Truncator

def post_list(request):
    # Fetch the search query from the request
    query = request.GET.get('q')
    
    if query:
        # Filter posts by the search query
        posts = Post.objects.filter(content__icontains=query).order_by('-created_at')
    else:
        # Fetch all posts if no search query is provided
        posts = Post.objects.all().order_by('-created_at')
    
    # Truncate the content of each post for display purposes
    for post in posts:
        post.truncated_content = Truncator(post.content).chars(100, truncate='...')  # Truncate to 100 characters
        
        # Attach the first image to the post
        if post.images.exists():
            post.first_image = post.images.first()
        else:
            post.first_image = None
    
    # Render the template with the posts
    return render(request, 'myapp/post_list.html', {'posts': posts})


from django.shortcuts import render, get_object_or_404

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Render the post detail template without comments or comment form
    return render(request, 'myapp/post_detail.html', {'post': post})


from django.shortcuts import render
from .models import Post

def gallery(request):
    # Fetch all images from posts
    images = []
    posts = Post.objects.all()
    for post in posts:
        for image in post.images.all():
            images.append({
                'image': image,
                'post': post
            })
    
    return render(request, 'myapp/gallery.html', {'images': images})

from django.shortcuts import render
from .models import Post

def videos(request):
    # Fetch all videos from posts
    videos = []
    posts = Post.objects.all()
    for post in posts:
        for video in post.videos.all():
            videos.append({
                'video': video,
                'post': post
            })
    
    return render(request, 'myapp/videos.html', {'videos': videos})











