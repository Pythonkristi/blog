from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm


# Создайте здесь свои представления.

def index(request):
	"""Домашняя страница приложения Blog"""
	title = BlogPost.objects.all()
	text = BlogPost.objects.order_by('-date_added')
	context = {'title': title, 'text': text}
	return render(request, 'blogs/index.html', context)

@login_required
def new_text(request):
	"""Определяет новую запись"""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма
		form = BlogPostForm()
	else:
		# Отправлены данные POST; обработать данные
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			new_text= form.save(commit=False)
			new_text.owner = request.user
			new_text.save()
			return redirect('blogs:index')

	# Вывести пустую или недействительную форму
	context = {'form': form}
	return render(request, 'blogs/new_text.html', context)

@login_required
def edit_text(request, texts_id):
	"""Редактирует существующую запись"""
	texts = BlogPost.objects.get(id=texts_id)
	check_text_owner(texts, request)
	if request.method != 'POST':
		# Исходный запрос; форма заполняется данными текущей записи
		form = BlogPostForm(instance=texts)
	else:
		# Отправка данных POST; обработать данные
		form = BlogPostForm(instance=texts, data=request.POST)
		if form.is_valid():

			form.save()
			return redirect('blogs:index')

	context = { 'texts': texts, 'form': form}
	return render(request, 'blogs/edit_text.html', context)

def check_text_owner(texts, request):
	if texts.owner != request.user:
		raise Http404