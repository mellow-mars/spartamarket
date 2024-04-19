from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Posts
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.db.models import Count
from django.db.models import Q


@require_GET
def index(request):
    order = request.GET.get('order', 'recent')
    if order == 'recent':
        posts = Posts.objects.order_by('-created_at')
    elif order == 'popular':
        posts = Posts.objects.annotate(popular=Count(
            'like_users')).order_by('-popular', '-created_at')
    context = {
        'posts': posts,
        'order': order
    }
    return render(request, 'products/index.html', context)


def search_results(request):
    query = request.GET.get('query')
    posts = Posts.objects.filter(
        Q(title__contains=query) |
        Q(content__contains=query) |
        Q(user__username__contains=query)
    )
    context = {
        'posts': posts
    }
    return render(request, 'products/index.html', context)



@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("index")
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "products/create_post.html", context)


@require_GET
def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    context = {'post': post}
    return render(request, 'products/post_detail.html', context)


@require_http_methods(["GET", "POST"])
def post_update(request, pk):
    post = Posts.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('products:post_detail', post.pk)
    else:
        form = PostForm(instance=post)
        context = {
            'form': form,
            'post': post,
        }
    return render(request, 'products/post_update.html', context)


@require_POST
def post_delete(request, pk):
    if request.method == "POST":
        article = Posts.objects.get(pk=pk)
        article.delete()
        return redirect("index")
    return redirect("products:post_detail", pk)


@require_POST
def post_like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Posts, pk=pk)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('index')
    return redirect('accounts:login')
