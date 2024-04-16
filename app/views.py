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
  return render(request, 'app/pyLevels/pyIntro.html')
@login_required
def pyLevel1(request):
  return render(request, 'app/pyLevels/pyLevel1.html')
@login_required
def pyLevel2(request):
  return render(request, 'app/pyLevels/pyLevel2.html')
@login_required
def pyLevel3(request):
  return render(request, 'app/pyLevels/pyLevel3.html')
@login_required
def pyLevel4(request):
  return render(request, 'app/pyLevels/pyLevel4.html')
@login_required
def pyLevel5(request):
  return render(request, 'app/pyLevels/pyLevel5.html')
@login_required
def pyLevel6(request):
  return render(request, 'app/pyLevels/pyLevel6.html')
@login_required
def pyTest1(request):
  return render(request, 'app/pyTests/pyTest1.html')
@login_required
def pyTest2(request):
  return render(request, 'app/pyTests/pyTest2.html')
@login_required
def pyTest3(request):
  return render(request, 'app/pyTests/pyTest3.html')
@login_required
def pyTest4(request):
  return render(request, 'app/pyTests/pyTest4.html')
@login_required
def pyTest5(request):
  return render(request, 'app/pyTests/pyTest5.html')
@login_required
def pyTest6(request):
  return render(request, 'app/pyTests/pyTest6.html')

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
  return render(request, 'app/javaLevels/javaIntro.html')
@login_required
def javaLevel1(request):
  return render(request, 'app/javaLevels/javaLevel1.html')
@login_required
def javaLevel2(request):
  return render(request, 'app/javaLevels/javaLevel2.html')
@login_required
def javaLevel3(request):
  return render(request, 'app/javaLevels/javaLevel3.html')
@login_required
def javaLevel4(request):
  return render(request, 'app/javaLevels/javaLevel4.html')
@login_required
def javaLevel5(request):
  return render(request, 'app/javaLevels/javaLevel5.html')
@login_required
def javaLevel6(request):
  return render(request, 'app/javaLevels/javaLevel6.html')
@login_required
def javaTest1(request):
  return render(request, 'app/javaTests/javaTest1.html')
@login_required
def javaTest2(request):
  return render(request, 'app/javaTests/javaTest2.html')
@login_required
def javaTest3(request):
  return render(request, 'app/javaTests/javaTest3.html')
@login_required
def javaTest4(request):
  return render(request, 'app/javaTests/javaTest4.html')
@login_required
def javaTest5(request):
  return render(request, 'app/javaTests/javaTest5.html')
@login_required
def javaTest6(request):
  return render(request, 'app/javaTests/javaTest6.html')

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
  return render(request, 'app/jsLevels/jsIntro.html')
@login_required
def jsLevel1(request):
  return render(request, 'app/jsLevels/jsLevel1.html')
@login_required
def jsLevel2(request):
  return render(request, 'app/jsLevels/jsLevel2.html')
@login_required
def jsLevel3(request):
  return render(request, 'app/jsLevels/jsLevel3.html')
@login_required
def jsLevel4(request):
  return render(request, 'app/jsLevels/jsLevel4.html')
@login_required
def jsLevel5(request):
  return render(request, 'app/jsLevels/jsLevel5.html')
@login_required
def jsLevel6(request):
  return render(request, 'app/jsLevels/jsLevel6.html')
@login_required
def jsTest1(request):
  return render(request, 'app/jsTests/jsTest1.html')
@login_required
def jsTest2(request):
  return render(request, 'app/jsTests/jsTest2.html')
@login_required
def jsTest3(request):
  return render(request, 'app/jsTests/jsTest3.html')
@login_required
def jsTest4(request):
  return render(request, 'app/jsTests/jsTest4.html')
@login_required
def jsTest5(request):
  return render(request, 'app/jsTests/jsTest5.html')
@login_required
def jsTest6(request):
  return render(request, 'app/jsTests/jsTest6.html')