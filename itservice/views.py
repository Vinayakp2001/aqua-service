from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'itservice/home.html')

def about(request):
    return render(request, 'itservice/about.html')

def contact(request):
    return render(request, 'itservice/contact.html')

def dashboard(request):
    # Example data (baad me yaha DB ya automation ka data aa sakta hai)
    context = {
        "services_done": 120,
        "services_pending": 30,
        "clients": 15
    }
    return render(request, 'itservice/dashboard.html', context)
