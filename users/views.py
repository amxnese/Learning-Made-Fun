from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as log, logout as out
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage

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
      return redirect('/main')
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

@login_required
def logout(request):
  out(request)
  messages.success(request, 'You have been logged out')
  return redirect('../')

@login_required
def profile(request):
  user = request.user
  if request.method == "POST" and request.FILES['profile_picture']:
    if user.profile_picture:
      old_picture_path = user.profile_picture.path
      if default_storage.exists(old_picture_path):
        default_storage.delete(old_picture_path)
    pic = request.FILES.get('profile_picture')
    user.profile_picture = pic
    user.save()
    return redirect('/profile')
  context = {
    'python' : int(user.python * 50 / 3) +20,
    'java' : int(user.java * 50 / 3)+2,
    'javaScript' : int(user.javaScript * 50 / 3)+50,
    'pic' : user.profile_picture.url if user.profile_picture else ""
  }
  return render(request, 'users/profile.html',{'info':context})

@login_required
def edit(request):
  if request.method == 'POST':
    user = request.user
    username = request.POST.get('username')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    user.username = username if username else user.username
    user.first_name = fname if fname else user.first_name
    user.last_name = lname if lname else user.last_name
    user.email = email if email else user.email
    user.save()
    messages.success(request, 'Profile updated successfully')
    return render(request, 'app/home.html')
  else:
    return render(request, 'users/edit.html')

@login_required
def change_password(request):
  if request.method == 'POST':
    user = request.user
    old = request.POST.get('old')
    new = request.POST.get('new')
    confirm = request.POST.get('confirm')
    if not user.check_password(old):
      messages.error(request, 'Wrong password!')
      return render(request, 'users/passwd.html')
    if new != confirm:
      messages.error(request, "Passwords don't match")
      return render(request, 'users/passwd.html')
    user.set_password(new)
    user.save()
    messages.success(request, 'Updated password successfully')
    return render(request, 'app/home.html')
  else:
    return render(request, 'users/passwd.html')

@login_required
def delete(request):
  user = request.user
  user.delete()
  return render(request, 'users/delete.html')
