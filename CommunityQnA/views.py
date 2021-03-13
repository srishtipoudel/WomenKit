from django.shortcuts import render

# Create your views here.

def lilacs(request):
    return render(request, 'lilacs.html')

