from django.db import models

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	admin = models.CharField(max_length=255)
	class Meta:
		db_table = 'users'

class Item(models.Model):
	item = models.CharField(max_length=255)
	user = models.ForeignKey(User)
	class Meta:
		db_table = 'items'

class Wishlist(models.Model):
	item = models.ForeignKey(Item)
	user = models.ForeignKey(User)
	class Meta:
		db_table = 'wishlist'