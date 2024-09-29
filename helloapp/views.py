from django.shortcuts import render
from django.http import HttpResponse 
 
def hifirst(request):
  return HttpResponse("Hello from App")

def myinfo(request):
    return render(request, 'helloapp/base.html')

def myquery(request):
    return render(request, 'helloapp/query.html')
