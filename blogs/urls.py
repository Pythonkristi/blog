"""Определяет схемы URL для blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
	# Домашняя страница
	path('', views.index, name='index'),
	# Страница для добавления новой записи
	path('new_text/', views.new_text, name='new_text'),
	# Страница для редактирования записи
	path('edit_text/<int:texts_id>', views.edit_text, name='edit_text'),
]