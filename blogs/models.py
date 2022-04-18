from django.db import models
from django.contrib.auth.models import User

# Создайте здесь свои модели.

class BlogPost(models.Model):
	"""Создание простого блога для пользователей"""
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Возвращает строковое предсавление модели"""
		return self.title
