"""Platzigram views"""
from django.http import HttpResponse
#utilities
from datetime import datetime
import json

def hello_world(request):
    
    return HttpResponse('Hi , current server time is {now}' .format(
        now=datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs')
        ))

def sorted_(request):
    """Return Json response with sorted list"""
    #import pdb; pdb.set_trace() debbuger : ej request.get.. 
    #print(request) #imprime la instancia del request
   
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    
    sorted_ints= sorted(numbers)
    data ={
        'status' : 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted successfully'
    }
    print(data)
    return HttpResponse(json.dumps(data)) #retorna json


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message= 'Sorry {}, ure not allowed here' .format(name)
    else:
        message= 'Hello {}, welcome to platzigram'.format(name)
    return HttpResponse(message)