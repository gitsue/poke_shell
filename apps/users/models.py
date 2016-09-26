from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def login(self, user_name):
		user = self.filter(user_name=user_name)
		if user:
			user = user[0]
		else:
			user = self.create(user_name=user_name)

		return user

class User(models.Model):
	user_name = models.CharField(max_length=255)
	objects = UserManager()