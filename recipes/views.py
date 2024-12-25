from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
#HTTP Request
def home(request):
    return render(request,'global/home.html', context={
        'name':'Dayuã Santana',
    })
    #Return HTTP Response
    
def contato(request):
    return render(request,'me-apague/temp.html')
    #Return HTTP Response

def sobre(request):
    return HttpResponse('Sobre')
    #Return HTTP Response