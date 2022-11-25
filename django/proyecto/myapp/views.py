from django.shortcuts import render
from django.http import HttpResponse


#This class is a Request Handler, it is like a controller. It does not contain vies nor html code nor templates.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Migue'})
