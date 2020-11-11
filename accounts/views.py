from django.shortcuts import render,redirect
from  .forms import UserForm,UserEditForm,ProfileEditForm
from .models import  Profile
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate, login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile')

    else:
        form = UserForm()
    return render(request, 'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})


@login_required
def profile_edit(request,id):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserEditForm(request.POST, instance=request.user)
        profileform = ProfileEditForm(request.POST, instance=profile)
        if userform.is_valid() and  profileform.is_valid():
            userform.save()
            myform = profileform.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')

    else:
        userform=UserEditForm(instance=request.user)
        profileform=ProfileEditForm(instance=profile)

    return render(request,'accounts/edit-profile.html',{'profile':profile,
                                                        'profileform':profileform,
                                                        'userform':userform})