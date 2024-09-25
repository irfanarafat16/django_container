from django import forms 
  
# creating a form  
class InputForm(forms.Form): 
    name = forms.CharField(max_length = 5) 
    address = forms.CharField(max_length = 5) 
