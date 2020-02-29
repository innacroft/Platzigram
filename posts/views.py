"""post views"""
#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#forms
from posts.forms import PostForm
#models
from posts.models import Post
# #utlilities

# Create your views here.

@login_required
def list_posts(request):
    """List existing posts."""
    posts=Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html',{'posts': posts})

@login_required
def create_post(request):
    """Creating new posts"""
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES) #crea el formulario con los datos que vengan en request
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else: #si el form no es post
        form=PostForm() #instancia del form vacio
    return render(request=request,
    template_name='posts/new.html',
    context={
        'form':form,
        'user':request.user,
        'profile': request.user.profile
        }
    )

    

