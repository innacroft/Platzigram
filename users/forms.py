"""User forms"""
#django
from django import forms 

from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
  """signup Form"""
  username= forms.CharField(min_length=4,max_length=50)

  password= forms.CharField(max_length=70,widget= forms.PasswordInput())
  password_confirmation= forms.CharField(
    max_length=70,
    widget= forms.PasswordInput())

  first_name= forms.CharField(min_length=2,max_length=50)
  last_name= forms.CharField(min_length=2,max_length=50)
  email=forms.CharField(min_length=6,
    max_length=70,
    widget=forms.EmailInput()
  )

def clean_username(self):
  """username must be unique"""
  username= self.cleaned_data['username'] #django crea un diccionario cleaned_data donde entrega los datos limpios 
  username_taken= User.objects.filter(username=username).exist #se crea un filtro que traiga el valor de username , si lo encuentra trae true si no false
  if username_taken :
    raise forms.ValidationError('Username is already in use')
  return username #importante siempre retornar el campo!! 

def clean(self): # aca hace validacion de campos que dependen unos de otros
  """verify password confirmation match"""
  data= super().clean #trae la data antes de ser sobreescrita
  password=data['password']
  password_confirmation=data['password_confirmation']

  if password != password_confirmation:
    raise forms.ValidationError('Passwords dont match')
  return data

def save(self): #guaraado de datos
  """create user and profile"""
  data= self.cleaned_data
  data.pop('password_confirmation')
  user = User.objects.create_user(**data) # aca s envia todo el diccionario **data
  profile=Profile(user=user)
  profile.save()


class ProfileForm(forms.Form):
  """profile form"""
  website= forms.URLField(max_length=200, required=True)
  biography= forms.CharField(max_length=500, required=False) 
  phone_number= forms.CharField(max_length=20, required=False)
  picture = forms.ImageField()