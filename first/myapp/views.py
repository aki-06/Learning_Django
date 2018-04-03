# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	"""
	/トップページ
	"""
	context = {
		'name': 'Aki'
	}
	return render(request, 'myapp/index.html', context)

def about(request):
	"""
	/about
	"""
	return render(request, 'myapp/about.html')

def info(request):
	"""
	/info
	"""
	return render(request, 'myapp/info.html')