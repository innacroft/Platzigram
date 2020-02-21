"""post views"""
from django.shortcuts import render
from datetime import datetime

posts=[
   { 
       'title':'Photoshop',
        'user':
        {
            'name': 'Maria Rodriguez',
            'picture': 'https://picsum.photos/60/60'

        } ,
          'timestamp': datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs'),
          'photo':'https://picsum.photos/800/800/'
   },

   { 
       'title':'Colors',
        'user':
        {
            'name': 'Juan Romero',
            'picture': 'https://picsum.photos/60/60'

        } ,
          'timestamp': datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs'),
          'photo': 'https://picsum.photos/800/800/'

   },

   { 
       'title':'Travel to the moon',
        'user':
        {
            'name': 'Ana Jimenez',
            'picture': 'https://picsum.photos/60/60'

        } ,
          'timestamp': datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs'),
          'photo':'https://picsum.photos/800/800/'
   }


  
    ]



def list_posts(request):

    return render(request,'feed.html',{'posts': posts})

# Create your views here.
