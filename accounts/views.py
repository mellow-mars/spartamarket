from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST,require_http_methods
from django.contrib.auth import get_user_model


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or 'index'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, username):
    user = get_user_model().objects.get(username=username)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance=user)
    context = {"form": form}
    return render(request, "accounts/user_update.html", context)


@require_POST
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('index')



