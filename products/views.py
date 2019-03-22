from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'object':obj,
	}
	#return HttpResponse("suvro")
	return render(request,"products/product_detail.html",context)