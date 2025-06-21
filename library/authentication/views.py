from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('home')
        return HttpResponse("Невірні дані або неактивний акаунт")
    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Ви успішно вийшли з системи.")
    return redirect('login')

def user_list_view(request):
    if not request.user.is_authenticated or request.user.role != 1:
        return render(request, '403.html')

    users = CustomUser.objects.all()
    return render(request, 'authentication/user_list.html', {'users': users})


def user_detail_view(request, user_id):
    if not request.user.is_authenticated:
        return render(request, '403.html')

    user = get_object_or_404(CustomUser, id=user_id)

    if request.user.role != 1 and request.user.id != user.id:
        return render(request, '403.html')

    return render(request, 'authentication/user_detail.html', {'user_obj': user})

@login_required
def home_view(request):
    return render(request, 'authentication/home.html', {'user': request.user})