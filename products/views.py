from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

from .forms import PureForm,ProductForm

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
 		#data is clean
 		print(form.cleaned_data)
 		Product.objects.create(**form.cleaned_data)
	context = {
		"form":form
	}
	return render(request,"products/product_create.html",context)


#pure django form
# from .forms import PureForm
# def product_create_view(request):
# 	#form = PureForm(request.POST or None)//its can be use without if else 
# 	if request.method == 'GET':
# 		form = PureForm()
# 	elif request.method == 'POST':
# 		form = PureForm(request.POST)
# 		if form.is_valid():
# 			#data is clean
# 			print(form.cleaned_data)
# 			Product.objects.create(**form.cleaned_data)
			

# 	context = {
# 		"form":form
# 	}
# 	return render(request,"products/product_create.html",context)


#raw html form
# def product_create_view(request):
# 	if request.method == 'POST':


# 		my_title = request.POST.get('title')
# 		my_description = request.POST.get('description')
# 		my_summary = request.POST.get('summary')
# 		my_featured = request.POST.get('featured')
# 		if request.POST.get('featured')  == None:
# 			my_featured = 0
# 		my_price = request.POST.get('price')
# 		print(my_title)
# 		print(my_description)
# 		print(my_summary)
# 		print(my_featured)
# 		print(my_price)
# 		#save data
# 		Product.objects.create(title=my_title,description=my_description,price=my_price,summary=my_summary,featured=my_featured)

# 	context = {}
# 	return render(request,"products/product_create.html",context)

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'object':obj,
	}
	#return HttpResponse("suvro")
	return render(request,"products/product_detail.html",context)