from django.shortcuts import render
from .forms import MemberForm
from django.contrib import messages
from .models import Member

def login(request):
  return render(request, 'users/login.html')

def register(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    if password != confirm:
      messages.error(request, "passwords don't match")
      return render(request, 'users/register.html')
    if Member.objects.filter(username=username):
      messages.error(request, "username not available")
      return render(request, 'users/register.html')
    form = MemberForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"account for {username} was created successfully")
      return render(request, 'app/home.html')
  else:
    return render(request, 'users/register.html')