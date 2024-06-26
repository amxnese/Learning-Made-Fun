from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.safestring import mark_safe
from users.models import Comment, CustomUser

def fetch(request, size):
  lst = []
  for i in range(1, size + 1):
    try:
      lst.append(request.POST[f'q{i}'])
    except KeyError:
      messages.warning(request, "Please make sure you answered all the questions")
      return False
  return lst

def calc_score(answers, to_check):
  score = 0
  for i in range(0, len(answers)):
    score = score + 1 if answers[i] == to_check[i] else score
  return score

def validate(request, score, full_mark, level, language):
  passing_grade = int(full_mark * 75 / 100)
  user = request.user
  current_level = getattr(user, language)
  print(current_level)
  if current_level != level-1:
    messages.success(request, f"You passed the test again and scored {score}/{full_mark}")
  elif score >= passing_grade:
    current_level += 1
    setattr(user, language, current_level)
    user.save()
    messages.success(request, mark_safe(f"<strong>Congratulations</strong>, You scored {score}/{full_mark} and has made it to the next level"))
  else:
      messages.warning(request, f"You failed the test with a score of {score}/{full_mark}, better luck next time")

def home(request):
  if request.method == "POST":
    user = request.user
    if user.is_authenticated:
      user_comment = request.POST.get('comment')
      comment = Comment.objects.create(user=user, content=user_comment)
      messages.error(request, "Your comment was added successfully")
      return redirect('/')
    else:
      messages.warning(request, "You need to log in so you can comment")
      return redirect('/')
  
  comments = Comment.objects.all()
  for i in comments:
    try:
      i.profile_pic = str(f"{CustomUser.objects.get(id=i.user_id).profile_picture.url}")
    except ValueError:
      pass
    i.user_id = CustomUser.objects.get(id=i.user_id)
  return render(request, 'app/home.html', {'comments': comments})

def main(request):
  if request.method == 'POST':
    results = request.POST.get('input')
    if not results:
      print('no results')
      return redirect('./')
    results = results.split(' ')
    result = None
    for course in results:
      if course.lower() == 'python' or course.lower() == 'py':
        result = 'python'
      elif course.lower() == 'javascript' or course.lower() == 'js':
        result = 'js'
      elif course.lower() == 'java':
        result = 'java'
      elif course.lower() == 'c':
        result = 'c'
      elif course.lower() == 'cpp' or course.lower() == 'c++':
        result = 'c++'
      elif course.lower() == 'sql' or course.lower() == 'database' or course.lower() == 'mysql':
        result = 'mysql'
      elif course.lower() == 'html' or course.lower() == 'front-end' or course.lower() == 'frontend':
        result = 'html'
      elif course.lower() == 'css' or course.lower() == 'front-end' or course.lower() == 'frontend':
        result = 'css'
      elif course.lower() == 'php' or course.lower() == 'backend':
        result = 'php'
      else:
        print('no results')
        messages.warning(request, "Can't find any results related to your search")
        return redirect('./')
      return render(request, 'app/main.html', {'result' : result})
  return render(request, 'app/main.html')

@login_required
def python(request):
  user = request.user
  lvl_py = user.python
  levels = ['secondary', 'secondary', 'secondary', 'secondary', 'secondary']
  try:
    for i in range(0, lvl_py):
      levels[i] = 'primary'
  except:
    pass
  lvl = {
    'lvl2':levels[0],
    'lvl3':levels[1],
    'lvl4':levels[2],
    'lvl5':levels[3],
    'lvl6':levels[4]
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
  if request.user.python < 1:
    return pyInvalid(request)
  return render(request, 'app/pyLevels/pyLevel2.html')

@login_required
def pyLevel3(request):
  if request.user.python < 2:
    return pyInvalid(request)
  return render(request, 'app/pyLevels/pyLevel3.html')

@login_required
def pyLevel4(request):
  if request.user.python < 3:
    return pyInvalid(request)
  return render(request, 'app/pyLevels/pyLevel4.html')

@login_required
def pyLevel5(request):
  if request.user.python < 4:
    return pyInvalid(request)
  return render(request, 'app/pyLevels/pyLevel5.html')

@login_required
def pyLevel6(request):
  if request.user.python < 5:
    return pyInvalid(request)
  return render(request, 'app/pyLevels/pyLevel6.html')

@login_required
def pyTest1(request):
  if request.method == "POST":
    answers = ['1','2','2','2','3','2','1','2','2','2','3','1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=1, language="python")
    return redirect('../')
  return render(request, 'app/pyTests/pyTest1.html')
  
@login_required
def pyTest2(request):
  if request.user.python < 1:
    return pyInvalid(request)
  if request.method == "POST":
    answers = ['2', '1', '2', '2', '1', '2', '1', '3', '3', '1', '2', '1', '1', '2', '2', '1', '1', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=2, language="python")
    return redirect('../')
  return render(request, 'app/pyTests/pyTest2.html')

@login_required
def pyTest3(request):
  if request.user.python < 2:
    return pyInvalid(request)
  if request.method == "POST":
    answers = ['2', '2', '1', '2', '3', '1', '1', '2', '2', '1', '1', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=3, language="python")
    return redirect('../')
  return render(request, 'app/pyTests/pyTest3.html')

@login_required
def pyTest4(request):
  if request.user.python < 3:
    return pyInvalid(request)
  if request.method == "POST":
    answers = ['1', '2', '2', '2', '3', '2', '3', '3']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=4, language="python")
    return redirect('../')
  return render(request, 'app/pyTests/pyTest4.html')

@login_required
def pyTest5(request):
  if request.user.python < 4:
    return pyInvalid(request)
  if request.method == "POST":
    answers = ['1', '1', '1', '2', '3', '2', '1', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=5, language="python")
    return redirect('../')
  return render(request, 'app/pyTests/pyTest5.html')

@login_required
def pyTest6(request):
  if request.user.python < 5:
    return pyInvalid(request)
  if request.method == "POST":
    answers = ['1', '2', '1', '1', '2', '2', '2', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=6, language="python")
    return redirect('../')
  return render(request, 'app/pyTests/pyTest6.html')

@login_required
def pyVideos(request):
  return render(request, 'app/pyVideos.html')

@login_required
def pyBooks(request):
  return render(request, 'app/pyBooks.html')

@login_required
def pyInvalid(request):
  print('hello')
  messages.info(request, "Oops! It seems like you haven't unlocked this level yet. Keep exploring and learning to unlock more exciting content! 🚀")
  return redirect('../')

@login_required
def java(request):
  user = request.user
  lvl_java = user.java
  levels = ['secondary', 'secondary', 'secondary', 'secondary', 'secondary']
  try:
    for i in range(0, lvl_java):
      levels[i] = 'primary'
  except:
    pass
  lvl = {
    'lvl2':levels[0],
    'lvl3':levels[1],
    'lvl4':levels[2],
    'lvl5':levels[3],
    'lvl6':levels[4]
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
  if request.user.java < 1:
    return javaInvalid(request)
  return render(request, 'app/javaLevels/javaLevel2.html')

@login_required
def javaLevel3(request):
  if request.user.java < 2:
    return javaInvalid(request)
  return render(request, 'app/javaLevels/javaLevel3.html')

@login_required
def javaLevel4(request):
  if request.user.java < 3:
    return javaInvalid(request)
  return render(request, 'app/javaLevels/javaLevel4.html')

@login_required
def javaLevel5(request):
  if request.user.java < 4:
    return javaInvalid(request)
  return render(request, 'app/javaLevels/javaLevel5.html')

@login_required
def javaLevel6(request):
  if request.user.java < 5:
    return javaInvalid(request)
  return render(request, 'app/javaLevels/javaLevel6.html')

@login_required
def javaTest1(request):
  if request.method == "POST":
    answers = ['1', '2', '1', '3', '2', '2', '2', '2', '1', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=1, language="java")
    return redirect('../')
  return render(request, 'app/javaTests/javaTest1.html')

@login_required
def javaTest2(request):
  if request.user.java < 1:
    return javaInvalid(request)
  if request.method == "POST":
    answers = ['2', '1', '3', '1', '2', '2', '1', '2', '2', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score, full_mark=len(answers), level=2, language="java")
    return redirect('../')
  return render(request, 'app/javaTests/javaTest2.html')

@login_required
def javaTest3(request):
  if request.user.java < 2:
    return javaInvalid(request)
  if request.method == "POST":
    answers = ['2', '1', '2', '2', '1', '1', '2', '2', '1', '3']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=3, language="java")
    return redirect('../')
  return render(request, 'app/javaTests/javaTest3.html')

@login_required
def javaTest4(request):
  if request.user.java < 3:
    return javaInvalid(request)
  if request.method == "POST":
    answers = ['1', '2', '2', '2', '2', '1', '1', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=4, language="java")
    return redirect('../')
  return render(request, 'app/javaTests/javaTest4.html')

@login_required
def javaTest5(request):
  if request.user.java < 4:
    return javaInvalid(request)
  if request.method == "POST":
    answers = ['1', '1', '1', '1', '1', '2', '2', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=5, language="java")
    return redirect('../')
  return render(request, 'app/javaTests/javaTest5.html')

@login_required
def javaTest6(request):
  if request.user.java < 5:
    return javaInvalid(request)
  if request.method == "POST":
    answers = ['1', '2', '1', '2', '2', '1', '1', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=6, language="java")
    return redirect('../')
  return render(request, 'app/javaTests/javaTest6.html')

@login_required
def javaVideos(request):
  return render(request, 'app/javaVideos.html')  

@login_required
def javaBooks(request):
  return render(request, 'app/javaBooks.html')

@login_required
def javaInvalid(request):
  messages.info(request, "Oops! It seems like you haven't unlocked this level yet. Keep exploring and learning to unlock more exciting content! 🚀")
  return redirect('../')

@login_required
def js(request):
  user = request.user
  lvl_js = user.javaScript
  levels = ['secondary', 'secondary', 'secondary', 'secondary', 'secondary']
  try:
    for i in range(0, lvl_js):
      levels[i] = 'primary'
  except:
    pass
  lvl = {
    'lvl2':levels[0],
    'lvl3':levels[1],
    'lvl4':levels[2],
    'lvl5':levels[3],
    'lvl6':levels[4]
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
  if request.user.js < 1:
    return jsInvalid(request)
  return render(request, 'app/jsLevels/jsLevel2.html')

@login_required
def jsLevel3(request):
  if request.user.js < 2:
    return jsInvalid(request)
  return render(request, 'app/jsLevels/jsLevel3.html')

@login_required
def jsLevel4(request):
  if request.user.js < 3:
    return jsInvalid(request)
  return render(request, 'app/jsLevels/jsLevel4.html')

@login_required
def jsLevel5(request):
  if request.user.js < 4:
    return jsInvalid(request)
  return render(request, 'app/jsLevels/jsLevel5.html')

@login_required
def jsLevel6(request):
  if request.user.js < 5:
    return jsInvalid(request)
  return render(request, 'app/jsLevels/jsLevel6.html')

@login_required
def jsTest1(request):
  if request.method == "POST":
    answers = ['1', '3', '2', '1', '2', '1', '2', '1', '2', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=1, language="javaScript")
    return redirect('../')
  return render(request, 'app/jsTests/jsTest1.html')

@login_required
def jsTest2(request):
  if request.user.js < 1:
    return jsInvalid(request)
  if request.method == "POST":
    answers = ['2', '2', '3', '2', '1', '2', '2', '1', '2', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=2, language="javaScript")
    return redirect('../')
  return render(request, 'app/jsTests/jsTest2.html')

@login_required
def jsTest3(request):
  if request.user.js < 2:
    return jsInvalid(request)
  if request.method == "POST":
    answers = ['2', '1', '1', '2', '3', '2', '2', '1', '2', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=3, language="javaScript")
    return redirect('../')
  return render(request, 'app/jsTests/jsTest3.html')

@login_required
def jsTest4(request):
  if request.user.js < 3:
    return jsInvalid(request)
  if request.method == "POST":
    answers = ['1', '2', '2', '1', '2', '3', '3', '2']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=4, language="javaScript")
    return redirect('../')
  return render(request, 'app/jsTests/jsTest4.html')

@login_required
def jsTest5(request):
  if request.user.js < 4:
    return jsInvalid(request)
  if request.method == "POST":
    answers = ['1', '3', '1', '1', '2', '1', '2', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=5, language="javaScript")
    return redirect('../')
  return render(request, 'app/jsTests/jsTest5.html')

@login_required
def jsTest6(request):
  if request.user.js < 5:
    return jsInvalid(request)
  if request.method == "POST":
    answers = ['1', '2', '2', '2', '3', '2', '2', '1']
    to_check = fetch(request, len(answers))
    if not to_check:
      return redirect('./')
    score = calc_score(answers, to_check)
    validate(request, score,  full_mark=len(answers), level=6, language="javaScript")
    return redirect('../')
  return render(request, 'app/jsTests/jsTest6.html')

@login_required
def jsVideos(request):
  return render(request, 'app/jsVideos.html')

@login_required
def jsBooks(request):
  return render(request, 'app/jsBooks.html')
  
@login_required
def jsInvalid(request):
  messages.info(request, "Oops! It seems like you haven't unlocked this level yet. Keep exploring and learning to unlock more exciting content! 🚀")
  return redirect('../')
