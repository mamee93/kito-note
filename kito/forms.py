from django import forms
from .models import  Kito,SameEat,Header,Comments

class AddKitoDay(forms.ModelForm):
    class Meta:
        model= Kito
        fields = ['title','img','content','Kg','day']

class AddCook(forms.ModelForm):
    class Meta:
        model= SameEat
        fields = ['title','image','content']

class AddHeader(forms.ModelForm):
    class Meta:
        model= Header
        fields = ['title','image','content']
       


class CommentForm(forms.ModelForm):
	
	comments = forms.CharField(label='', widget = forms.Textarea(attrs={'class':'from-control','placeholder':'Text here ','rows':'3', 'cols':'50'}))
	class Meta:
		model= Comments
		fields = ['comments']