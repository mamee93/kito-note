from django.shortcuts import render,redirect,get_object_or_404,Http404
from  .models import Kito,SameEat,Header,Comments
from  .forms import AddKitoDay,AddCook,CommentForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
# Create your views here.
def kito_list(request):
    user=request.user
    profile = Profile.objects.get(user=request.user)
    kito_post = Kito.objects.all()
    eat_cook = SameEat.objects.all()
    header = Header.objects.all()
   
    return render(request, 'kito_list.html',{'kito_post':kito_post,'eat_cook':eat_cook,'header':header,'profile':profile})
# def comments(request,id):
#     comments = Comments.objects.filter(Kito=Kito)
#     total_comments = comments.count()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             myform = form.save(commit=False)
#             myform.parent=comment_qs
#             myform.user = request.user
#             myform.Kito = Kito
#             myform.save()
#     else:
#         form = CommentForm()
#     return render(rquest, 'comments.html',{'form':form,'total_comments':total_comments})
@login_required
def add_daykito(request):
    request.user =user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddKitoDay(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('/')
    else:
        form =AddKitoDay()
    return render(request,'add-daykito.html',{'form':form,'profile':profile})

@login_required
def add_haeder(request):
    request.user =user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddKitoDay(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('/')
    else:
        form =AddKitoDay()
    return render(request,'add-header.html',{'form':form,'profile':profile})

@login_required
def edit_header(request, slug):
    request.user =user
    profile = Profile.objects.get(user=request.user)
    edit_header = get_object_or_404(Header, post_slug=slug)
    if request.method == 'POST':
        form = AddCook(request.POST, instance = edit_header)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.userheader = request.user
            new_form.save()
            return  redirect('/')
    else:
        form = AddCook(instance = edit_header)
    context = {
        'form': form,
        'profile':profile
    }
    return render(request, 'edit_header.html', context)

@login_required
def edit(request, slug):
    request.user =user
    profile = Profile.objects.get(user=request.user)
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
        'profile':profile
         
    }
    return render(request, 'create.html', context)


@login_required 
def add_cook(request):
    request.user =user
    profile = Profile.objects.get(user=request.user)
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
    request.user =user
    profile = Profile.objects.get(user=request.user)
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
        'profile':profile
    }
    return render(request, 'edit_cook.html', context)

@login_required
def list_delete(request, slug):

    post = get_object_or_404(Kito,post_slug=slug)
    if request.user != post.owner:
        raise Http404()
    post.delete()
    return redirect('kito:kito_list')