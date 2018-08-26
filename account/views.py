from django.shortcuts import render
from .forms import register, sign
from .models import User
from django.contrib.auth import authenticate, login ,logout


def index(request):
    return render(request, 'account/index.html')

def logoutview(request):
	logout(request)
	return render(request, 'account/index.html')


def registerview(request):
    form = register(request.POST or None)
    print(form.errors)
    if form.is_valid():
        user = form.save(commit=False)
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        user.set_password(password1)

        user.save()
        login(request, user)
        return render(request, 'account/index.html', {'user': user})

    else:

        return render(request, 'account/register.html', {'form': form})


def loginview(request):
    form = sign(request.POST)
    print(form.errors)
    if form.is_valid():
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.active:
                login(request, user)
                context = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
                return render(request, 'account/index.html', context)
