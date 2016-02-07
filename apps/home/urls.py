from django.conf.urls import patterns, url
from apps.home import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'register/', views.register, name='register'),
	url(r'login/', views.login, name='login'),
	url(r'dashboard/', views.dashboard, name='dashboard'),
	url(r'back/', views.back, name='back'),
	url(r'logout/', views.logout, name='logout'),
	url(r'add/', views.add, name='add'),
	url(r'search/?$', views.search, name='search'),
	url(r'create/', views.create, name='create'),
	url(r'random/', views.random, name='random'),
	url(r'delete/(?P<item_id>\d+)/', views.delete, name='delete'),
]