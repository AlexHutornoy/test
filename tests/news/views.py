from django.shortcuts import render
from .models import News

# Create your views here.
from django.http import HttpResponse


def index(request):
	news_list = News.objects.all()	
	context = {'News':news_list}
	return render(request, 'news.html', context)
