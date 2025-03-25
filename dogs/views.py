from django.shortcuts import render

from dogs.models import Breed,Dog
# Create your views here.
def index(request):
    context = {
        'objects_list':Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request,"dogs/index.html",context)