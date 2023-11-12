from django.shortcuts import render
from .forms import LoginForm, SignupForm

def home(request):
    return render(request, 'home.html', {})

def login(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            form = SignupForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
        else:
            form = LoginForm(request.POST)
    context = {
        's_form': SignupForm,
        'l_form': LoginForm
    }
    return render(request, 'login.html', context)