
"""user views"""
#django
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect

#exceptions
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from users.models import Profile

#forms
from users.forms import ProfileForm
# Create your views here.
@login_required
def update_profile(request):
  """Update user's Profile view"""
  
  profile=request.user.profile
  if request.method=='POST':
    form=ProfileForm(request.POST, request.FILES) #tipo de request post y admitir imagenes 
    if form.is_valid():
      data=form.cleaned_data #guardar los datos recibidos en data
      profile.website=data['website']
      profile.phone_number=data['phone_number']
      profile.biography=data['biography']
      profile.picture=data['picture']
      profile.save() #guardar toda la data en 
      print(form.cleaned_data)
      return redirect('update_profile') #esto evita que el formulario se reenvie
      
      
  else:
    form= ProfileForm()

  return render(request=request,
    template_name='users/update_profile.html',
    context={
      'profile': profile,
      'user': request.user,
      'form': form
    })


def login_view(request):
  """login view"""
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user= authenticate(request, username=username, password=password)
    print('new')
    if user:
      login(request,user)
      return redirect ('feed')
    else:
      return render( request, 'users/login.html', {'error':'invalid username and password'})
  return render( request, 'users/login.html')
  
def signup(request):
  """sign up view"""
  
  if request.method=='POST':
    username=request.POST['username']
    password= request.POST['passwd']
    passwd_confirmation= request.POST['passwd_confirmation']
    if password != passwd_confirmation:
      print('password is not the same')
      return render(request,'users/signup.html',{'error':'Passwords dont match'})
    try:
      user=User.objects.create_user(username=username,password=password)
    except IntegrityError:
      return render(request,'users/signup.html',{'error':'User already exists'})

    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email =request.POST['email']
    user.save() 
    
    profile=Profile(user=user) #tambien se puede profile.object.create
    profile.save()
    return redirect('login')
  return render(request,'users/signup.html')



@login_required
def logout_view(request):
  """logout a user"""
  return redirect('login')
  
