from django.shortcuts import render
# Create your views here.
#HTTP Request
def home(request):
    return render(request,'recipes/pages/home.html', context={
        'name':'Dayuã Santana',
    })
    #Return HTTP Response