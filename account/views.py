from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user login
            return redirect('articles:index')
    else:    
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            # login(request, user)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})
