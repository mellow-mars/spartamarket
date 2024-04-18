from arrow import get
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from numpy import require
from django.views.decorators.http import require_POST


# Create your views here.
def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    posts = profile.like_posts.all()
    context = {
        'profile': profile,
        'posts' : posts,
    }
    return render(request, 'users/profile.html', context)

@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        profile = get_object_or_404(get_user_model(), username=username)
        if profile != request.user:
            if profile.followers.filter(username=request.user.username).exists():
                profile.followers.remove(request.user)
            else:
                profile.followers.add(request.user)
        return redirect('users:profile', username=profile.username)
    return redirect('accounts:login')


