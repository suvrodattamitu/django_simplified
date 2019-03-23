from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from .models import Product

from .forms import PureForm,ProductForm

def product_list_view(request):
	obj = Product.objects.all()
	context = {
		'object_list':obj
	}
	return render(request,'products/product_list.html',context)

def product_delete_view(request,my_id):
	obj = get_object_or_404(Product,id=my_id)
	if request.method == 'POST':
		obj.delete()
		return redirect('/')
	context={
		'object':obj
	}

	return render(request,'products/product_delete.html',context)


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


def product_dynamic_view(request,my_id):
	#obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product,id=my_id)
	context = {
		'object':obj,
	}
	#return HttpResponse("suvro")
	return render(request,"products/product_detail.html",context)

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