from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from django.db import connection
#from .models import DataModel
from .forms import InputForm

def index(request):
    return HttpResponse("Hi world form cicd pipeline 2")

def contact(request):
    url = 'http://172.15.0.11:8000/contact/'
    response = requests.get(url)
    return HttpResponse(f'Mama: {response.text}')

def info(request):
    #return HttpResponse("InFo")
    return render(request, 'core/base.html')

def tdata(request):
    #patients = DataModel.objects.all()
    ####
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Persons")
    rows = cursor.fetchall()
    data = {'name':[],'address':[]}
    for r in rows:
        data['name'].append(r[1])
        data['address'].append(r[2])
    aaa = []
    for i in range(0,len(data['name']),1):
       aaa.append( {'name':data['name'][i], 'address':data['address'][i]} )
    print(aaa)
    return render(request, 'core/query.html', {'aaa':aaa})


def forminfo(request):
    context ={}
    if request.method == "POST":  
        form = InputForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            cursor = connection.cursor()
            #print(address)
            #print(name)
            cursor.execute(f"INSERT INTO Persons(name, address) VALUES('{name}', '{address}')")
            return redirect('/') 
    else:
        context['form']= InputForm()
    return render(request, 'core/myform.html', context)
