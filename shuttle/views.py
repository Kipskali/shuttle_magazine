from django.shortcuts import render, get_object_or_404
from .models import event, photo

# Create your views here.

def index(request):
    return render(request, 'shuttle/index.html')

def magazine(request):
    return render(request, 'shuttle/magazine.html')

def events(request):
    events = event.objects.all()
    return render(request, 'shuttle/events.html', {'events':events})

def pictorial(request):
  ###  events = event.objects.all()
    photos = photo.objects.all()
    return render(request, 'shuttle/pictorial.html', {
        ###'events':events,
        'photos':photos
    })