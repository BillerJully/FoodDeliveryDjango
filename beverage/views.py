from django.shortcuts import render
# Create your views here.
def beveragemain(request):
    return render(request, 'beverage/beveragemain.html')