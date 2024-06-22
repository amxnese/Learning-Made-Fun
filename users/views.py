from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as log, logout as out
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.contrib.auth import update_session_auth_hash
import os

def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    if not CustomUser.objects.filter(username=username):
      messages.error(request, f"{username} is not registered")
      return redirect('./')
    user = authenticate(request, username=username, password=password)
    if user:
      log(request, user)
      messages.success(request, f"You have successfully logged in, Welcome back {user.username}")
      return redirect('/main')
    else:
      messages.error(request, f"wrong password for {username}")
      return redirect('./')
  else:
    return render(request, 'users/login.html')

def register(request):
  if request.method == "POST":
    username = request.POST.get('username')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    if password != confirm:
      messages.error(request, "passwords don't match")
      return redirect('./')
    if len(password) < 8:
      messages.error(request, "password must have at least 8 characters")
      return redirect('./')
    if CustomUser.objects.filter(username=username):
      messages.warning(request, "username already taken")
      return redirect('./')
    CustomUser.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
    user = authenticate(request, username=username, password=password) 
    if user:
      log(request, user)
    # giving user default profile picture
    # pic = 'default.jpg'
    # user.profile_picture = pic
    user.save()
    # using defferent message tags to know where did the message came from
    messages.info(request, f"account for {username} was created successfully")
    return redirect('/main')
  else:
    return render(request, 'users/register.html')

@login_required
def logout(request):
  out(request)
  messages.success(request, 'You have been successfully logged out, Hope we see you soon!')
  return redirect('/')

@login_required
def profile(request):
  user = request.user
  if request.method == "POST" and request.FILES['profile_picture']:
    # deleting the old profile picture if the app is on production mode
    if os.environ.get('DJANGO_DEVELOPMENT'):
      if user.profile_picture and user.profile_picture != 'default.jpg':
        old_picture_path = user.profile_picture.path
        if default_storage.exists(old_picture_path):
          default_storage.delete(old_picture_path)
    pic = request.FILES.get('profile_picture')
    user.profile_picture = pic
    user.save()
    return redirect('./')
  context = {
    'python' : int(user.python * 50 / 3),
    'java' : int(user.java * 50 / 3),
    'javaScript' : int(user.javaScript * 50 / 3),
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
    password = request.POST.get('password')
    check_pwd = authenticate(request, username=user.username, password=password)
    if not check_pwd:
      messages.error(request, "Incorrect Password!")
      return redirect('./')
    if CustomUser.objects.filter(username=username) and user.username != username:
      messages.warning(request, "username already taken")
      return redirect('./')
    user.username = username
    user.first_name = fname
    user.last_name = lname
    user.save()
    # messages.success(request, 'Profile updated successfully')
    return redirect('../')
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
      messages.error(request, 'Incorrect password!')
      return redirect('./')
    if new != confirm:
      messages.error(request, "Passwords don't match")
      return redirect('./')
    if old == new:
      messages.error(request, "Your new password must be different from your previous password.")
      return redirect('./')
    user.set_password(new)
    user.save()
    update_session_auth_hash(request, user)  # Keeps the user logged in
    messages.success(request, 'changed')
    return redirect('/')
  else:
    return render(request, 'users/passwd.html')

@login_required
def delete(request):
  user = request.user
  # deleting the user's profile picture from database
  if user.profile_picture and user.profile_picture != 'default.jpg':
      old_picture_path = user.profile_picture.path
      if default_storage.exists(old_picture_path):
        default_storage.delete(old_picture_path)
  out(request)
  user.delete()
  messages.info(request, 'Your account has been successfully deleted!')
  return redirect('/')
