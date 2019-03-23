from django import forms
from .models import Product

#form using model
class ProductForm(forms.ModelForm):
	class Meta:
		model  = Product
		fields = [
			'title',
			'description',
			'price',
			'summary',
		]

	#validate form 
	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get('title')
		if  "suvro" in title:
			raise forms.ValidationError("this is not a valid title")
		return title




#form using pure django
class PureForm(forms.Form):
	title 		 = forms.CharField()
	description  = forms.CharField()
	summary      = forms.CharField()
	price 		 = forms.CharField()



