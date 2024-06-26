from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='app-home'),
  path('main/', views.main, name='app-main'),
  path('main/python/', views.python, name='app-py'),
  path('main/python/intro/', views.pyIntro, name='app-pyIntro'),
  path('main/python/level1/', views.pyLevel1, name='app-pyLevel1'),
  path('main/python/level2/', views.pyLevel2, name='app-pyLevel2'),
  path('main/python/level3/', views.pyLevel3, name='app-pyLevel3'),
  path('main/python/level4/', views.pyLevel4, name='app-pyLevel4'),
  path('main/python/level5/', views.pyLevel5, name='app-pyLevel5'),
  path('main/python/level6/', views.pyLevel6, name='app-pyLevel6'),
  path('main/python/test1/', views.pyTest1, name='app-pyTest1'),
  path('main/python/test2/', views.pyTest2, name='app-pyTest2'),
  path('main/python/test3/', views.pyTest3, name='app-pyTest3'),
  path('main/python/test4/', views.pyTest4, name='app-pyTest4'),
  path('main/python/test5/', views.pyTest5, name='app-pyTest5'),
  path('main/python/test6/', views.pyTest6, name='app-pyTest6'),
  path('main/python/videos/', views.pyVideos, name='app-pyVideos'),
  path('main/python/books/', views.pyBooks, name='app-pyBooks'),
  path('main/python/invalid/', views.pyInvalid, name='app-pyInvalid'),
  path('main/java/', views.java, name='app-java'),
  path('main/java/intro/', views.javaIntro, name='app-javaIntro'),
  path('main/java/level1/', views.javaLevel1, name='app-javaLevel1'),
  path('main/java/level2/', views.javaLevel2, name='app-javaLevel2'),
  path('main/java/level3/', views.javaLevel3, name='app-javaLevel3'),
  path('main/java/level4/', views.javaLevel4, name='app-javaLevel4'),
  path('main/java/level5/', views.javaLevel5, name='app-javaLevel5'),
  path('main/java/level6/', views.javaLevel6, name='app-javaLevel6'),
  path('main/java/test1/', views.javaTest1, name='app-javaTest1'),
  path('main/java/test2/', views.javaTest2, name='app-javaTest2'),
  path('main/java/test3/', views.javaTest3, name='app-javaTest3'),
  path('main/java/test4/', views.javaTest4, name='app-javaTest4'),
  path('main/java/test5/', views.javaTest5, name='app-javaTest5'),
  path('main/java/test6/', views.javaTest6, name='app-javaTest6'),
  path('main/java/videos/', views.javaVideos, name='app-javaVideos'),
  path('main/java/books/', views.javaBooks, name='app-javaBooks'),
  path('main/java/invalid/', views.javaInvalid, name='app-javaInvalid'),
  path('main/js/', views.js, name='app-js'),
  path('main/js/Intro/', views.jsIntro, name='app-jsIntro'),
  path('main/js/level1/', views.jsLevel1, name='app-jsLevel1'),
  path('main/js/level2/', views.jsLevel2, name='app-jsLevel2'),
  path('main/js/level3/', views.jsLevel3, name='app-jsLevel3'),
  path('main/js/level4/', views.jsLevel4, name='app-jsLevel4'),
  path('main/js/level5/', views.jsLevel5, name='app-jsLevel5'),
  path('main/js/level6/', views.jsLevel6, name='app-jsLevel6'),
  path('main/js/test1/', views.jsTest1, name='app-jsTest1'),
  path('main/js/test2/', views.jsTest2, name='app-jsTest2'),
  path('main/js/test3/', views.jsTest3, name='app-jsTest3'),
  path('main/js/test4/', views.jsTest4, name='app-jsTest4'),
  path('main/js/test5/', views.jsTest5, name='app-jsTest5'),
  path('main/js/test6/', views.jsTest6, name='app-jsTest6'),
  path('main/js/videos/', views.jsVideos, name='app-jsVideos'),
  path('main/js/books/', views.jsBooks, name='app-jsBooks'),
  path('main/js/invalid/', views.jsInvalid, name='app-jsInvalid'),
]
