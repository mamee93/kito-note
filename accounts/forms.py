from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from  .models import Profile
# from .models import

class UserForm(UserCreationForm):

    class  Meta:
        model = User
        fields = ['username','email','password1','password1']



class ProfileEditForm(forms.ModelForm):

    class  Meta:
    	
        model = Profile
        fields = ['user','image','bio']
        
class UserEditForm(forms.ModelForm):
    
    class  Meta:
        model = User
        fields = ['username','first_name','last_name','email']