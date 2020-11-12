from django.shortcuts import render,redirect,get_object_or_404,Http404
from  .models import Kito,SameEat,Header,Comments
from  .forms import AddKitoDay,AddCook,CommentForm,AddHeader
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
# Create your views here.
def kito_list(request):
    
    kito_post = Kito.objects.all()
    eat_cook = SameEat.objects.all()
    header = Header.objects.all()
   
    return render(request, 'kito_list.html',{'kito_post':kito_post,'eat_cook':eat_cook,'header':header})
def deleteList(request,slug):
    item = Kito.objects.get(post_slug=slug)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context ={'item':item}
    return render(request,'delete_list.html',context)




@login_required
def add_daykito(request):
     
    if request.method == 'POST':
        form = AddKitoDay(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('/')
    else:
        form =AddKitoDay()
    return render(request,'add-daykito.html',{'form':form })

@login_required
def add_haeder(request):
     
    if request.method == 'POST':
        form = AddHeader(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('/')
    else:
        form =AddHeader()
    return render(request,'add-header.html',{'form':form})

@login_required
def edit_header(request, slug):
    
    edit_header = get_object_or_404(Header, post_slug=slug)
    if request.method == 'POST':
        form = AddHeader(request.POST, instance = edit_header)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.userheader = request.user
            new_form.save()
            return  redirect('/')
    else:
        form = AddHeader(instance = edit_header)
    context = {
        'form': form,
         
    }
    return render(request, 'edit_header.html', context)
@login_required
def delete_header(request,slug):
    item = Header.objects.get(post_slug=slug)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context ={'item':item}
    return render(request,'delete_header.html',context)

@login_required
def edit(request, slug):
    
    edit_days = get_object_or_404(Kito, post_slug=slug)
    if request.method == 'POST':
        form = AddKitoDay(request.POST, instance = edit_days)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return  redirect('/')
    else:
        form = AddKitoDay(instance = edit_days)
    context = {
        'form': form,
         
         
    }
    return render(request, 'create.html', context)


@login_required 
def add_cook(request):
     
    if request.method == 'POST':
        form = AddCook(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/')
    else:
        form =AddCook()
    return render(request,'add-cook.html',{'form':form})

@login_required
def edit_cook(request, slug):
     
    edit_cook = get_object_or_404(SameEat, post_slug=slug)
    if request.method == 'POST':
        form = AddCook(request.POST, instance = edit_cook)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return  redirect('/')
    else:
        form = AddCook(instance = edit_cook)
    context = {
        'form': form,
         
    }
    return render(request, 'edit_cook.html', context)

@login_required
def delete_cook(request,slug):
    item = Header.objects.get(post_slug=slug)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context ={'item':item}
    return render(request,'delete_cook.html',context)