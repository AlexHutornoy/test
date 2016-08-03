from django.shortcuts import render,get_object_or_404
from .models import News
import feedparser

from django.shortcuts import render
import datetime


from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

from django.contrib import auth




#coding: utf-8



from django.http import HttpResponse


def index(request):
	d=feedparser.parse('http://feedparser.org/docs/examples/rss20.xml')

	news_list = News.objects.all()
	context = {'News':news_list}


	return render(request, 'news.html', context)

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
       
        form.save()
        return super(RegisterFormView, self).form_valid(form)
        



class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)

      
        return HttpResponseRedirect("/")

def login_view(request):
	uname = request.POST['username']
	pas = request.POST['password']
	user = auth.authenticate(username=uname,password=pas)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/login/")



def about(request, pk):
	news = get_object_or_404(News, pk = pk)

	context = {'news':news}
	return render(request,'about_news.html', context)





