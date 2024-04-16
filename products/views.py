from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Posts
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'products/index.html')


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

def post_detail(request):
    post = get_object_or_404(Posts, pk=pk)
    context = {'ppst': post}
    return render(request, 'posts/post_detail.html', context)
