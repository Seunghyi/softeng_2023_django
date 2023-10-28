from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# Create your views here.
#def index(request):
#    posts = Post.objects.all().order_by('-updated_at')
#
#    return render(
#        request,
#        "blog/post_list.html",
#        {
#            'posts': posts,
#        }
#    )

#def single_post_page(request, pkey):
#    post = Post.objects.get(pk=pkey)
#    return render(
#        request,
#        "blog/post_detail.html",
#        {'post': post},
#    )