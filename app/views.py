from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'app/home.html')

def main(request):
  return render(request, 'app/main.html')

@login_required
def python(request):
  user = request.user
  lvl_py = user.python
  hrefs = ['', '', '', '', '', '']
  levels = ['secondary', 'secondary', 'secondary', 'secondary', 'secondary', 'secondary']
  for i in range(0, lvl_py+1):
    levels[i] = 'primary'
  lvl = {
    'lvl1':levels[0],
    'lvl2':levels[1],
    'lvl3':levels[2],
    'lvl4':levels[3],
    'lvl5':levels[4],
    'lvl6':levels[5]
  }
  return render(request, 'app/python.html',{'levels':lvl})

@login_required
def pyIntro(request):
  return render(request, 'app/pyIntro.html')
@login_required
def pyLevel1(request):
  return render(request, 'app/pyLevel1.html')
@login_required
def pyLevel2(request):
  return render(request, 'app/pyLevel2.html')
@login_required
def pyLevel3(request):
  return render(request, 'app/pyLevel3.html')
@login_required
def pyLevel4(request):
  return render(request, 'app/pyLevel4.html')
@login_required
def pyLevel5(request):
  return render(request, 'app/pyLevel5.html')
@login_required
def pyLevel6(request):
  return render(request, 'app/pyLevel6.html')

@login_required
def java(request):
  user = request.user
  lvl_java = user.java
  levels = ['secondary', 'secondary', 'secondary', 'secondary', 'secondary', 'secondary']
  for i in range(0, lvl_java+1):
    levels[i] = 'primary'
  lvl = {
    'lvl1':levels[0],
    'lvl2':levels[1],
    'lvl3':levels[2],
    'lvl4':levels[3],
    'lvl5':levels[4],
    'lvl6':levels[5]
  }
  return render(request, 'app/java.html',{'levels':lvl})

@login_required
def javaIntro(request):
  return render(request, 'app/javaIntro.html')
@login_required
def javaLevel1(request):
  return render(request, 'app/javaLevel1.html')
@login_required
def javaLevel2(request):
  return render(request, 'app/javaLevel2.html')
@login_required
def javaLevel3(request):
  return render(request, 'app/javaLevel3.html')
@login_required
def javaLevel4(request):
  return render(request, 'app/javaLevel4.html')
@login_required
def javaLevel5(request):
  return render(request, 'app/javaLevel5.html')
@login_required
def javaLevel6(request):
  return render(request, 'app/javaLevel6.html')

@login_required
def js(request):
  user = request.user
  lvl_js = user.javaScript
  levels = ['secondary', 'secondary', 'secondary', 'secondary', 'secondary', 'secondary']
  for i in range(0, lvl_js+1):
    levels[i] = 'primary'
  lvl = {
    'lvl1':levels[0],
    'lvl2':levels[1],
    'lvl3':levels[2],
    'lvl4':levels[3],
    'lvl5':levels[4],
    'lvl6':levels[5]
  }
  return render(request, 'app/js.html',{'levels':lvl})

@login_required
def jsIntro(request):
  return render(request, 'app/jsIntro.html')
@login_required
def jsLevel1(request):
  return render(request, 'app/jsLevel1.html')
@login_required
def jsLevel2(request):
  return render(request, 'app/jsLevel2.html')
@login_required
def jsLevel3(request):
  return render(request, 'app/jsLevel3.html')
@login_required
def jsLevel4(request):
  return render(request, 'app/jsLevel4.html')
@login_required
def jsLevel5(request):
  return render(request, 'app/jsLevel5.html')
@login_required
def jsLevel6(request):
  return render(request, 'app/jsLevel6.html')