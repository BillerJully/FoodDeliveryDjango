from django.shortcuts import render
from django.http import HttpResponseNotFound
# Create your views here.

def foodmain(request):
    return render(request, 'food/foodmain.html')



def pageNotFound(request, exception):
    return render(request, 'food/notfound.html.html')