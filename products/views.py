from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Posts
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'products/index.html', context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("index")
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "products/create_post.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    context = {'post': post}
    return render(request, 'products/post_detail.html', context)


def post_update(request, pk):
    post = Posts.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            article = form.save()
            return redirect('products:post_detail', post.pk)
    else:
        form = PostForm(instance=post)
        context = {
            'form': form,
            'post': post,
        }
    return render(request, 'products/post_update.html', context)
