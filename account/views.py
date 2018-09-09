from django.shortcuts import render
from .forms import register, loggedin
from .models import User
from django.contrib.auth import authenticate, login, logout
from waste.models import complainform

def home(request):
    return render(request, 'account/base.html')


def logged(request):
    form = loggedin(request.POST or None)
    if form.is_valid():
        print(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            comp = complainform.objects.all()
            
            context = {
                'user': user,
                'comp':comp, }
            return render(request, 'account/base.html', context)
        else:
            return render(request, 'account/base.html')
    else:
        return render(request, 'account/base.html', {form: form})


def logoutview(request):
    logout(request)
    return render(request, 'account/base.html')


def registerview(request):
    form = register(request.POST or None)
    print(form.errors)
    if form.is_valid():
        user = form.save(commit=False)
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        user.set_password(password1)

        user.save()
        #login(request, user)
        return render(request, 'account/base.html', {'user': user})

    else:

        return render(request, 'account/register.html', {'form': form})


def complains(request):
    comp = complainform.objects.all()
    return render(request , 'account/base.html',{'comp':comp})

def analysisview(request):
    return render(request,'account/analysis.html')