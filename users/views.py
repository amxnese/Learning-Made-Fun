from django.shortcuts import render

def login(request):
  return render(request, 'users/login.html')

def register(request):
  return render(request, 'users/register.html')