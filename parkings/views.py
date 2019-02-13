from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'parkings/parkings.html')


def parking(request):
    return render(request, 'parkings/parking.html')

def search(request):
    return render(request, 'parkings/search.html')