from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
	return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
	return render(request,"about.html",{})

def blog_view(request,*args,**kwargs):
	return HttpResponse("<h1>Hello Blog</h1>")