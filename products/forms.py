from django import forms

class PureForm(forms.Form):
	title 		 = forms.CharField()
	description  = forms.CharField()
	summary      = forms.CharField()
	price 		 = forms.CharField()



