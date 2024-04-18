from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth import get_user_model


# Create your views here.
def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)