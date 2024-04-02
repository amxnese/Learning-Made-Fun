from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login as log, logout as out
from .models import CustomUser

def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    if not CustomUser.objects.filter(username=username):
      messages.error(request, f"{username} is not registered")
      return render(request, 'users/login.html')
    user = authenticate(request, username=username, password=password)
    if user:
      log(request, user)
      messages.success(request, "You have successfully logged in")
      return render(request, 'app/home.html')
    else:
      messages.error(request, f"wrong password for {username}")
      return render(request, 'users/login.html')
  else:
    return render(request, 'users/login.html')

def register(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    if password != confirm:
      messages.error(request, "passwords don't match")
      return render(request, 'users/register.html')
    if CustomUser.objects.filter(username=username):
      messages.error(request, "username not available")
      return render(request, 'users/register.html')
    user = CustomUser.objects.create_user(username=username, password=password)
    user1 = authenticate(request, username=username, password=password)
    if user1:
      log(request, user)
    messages.success(request, f"account for {username} was created successfully")
    return render(request, 'app/home.html')
  else:
    return render(request, 'users/register.html')

def logout(request):
  out(request)
  return render(request, 'users/logout.html')