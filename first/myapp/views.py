# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {
		'name': 'Aki'
	}
	return render(request, 'myapp/index.html', context)