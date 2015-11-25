from django.conf.urls import patterns, url
from apps.home import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'register/', views.register, name='register'),
	url(r'login/', views.login, name='login'),
	url(r'dashboard/', views.dashboard, name='dashboard'),
	url(r'back/', views.back, name='back'),
	url(r'add', views.add, name='add'),
]