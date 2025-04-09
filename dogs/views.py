from PIL.ImageFilter import DETAIL
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy
from dogs.models import Breed, Dog
from dogs.forms import DogForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here
def index(request):
    context = {
        'objects_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, "dogs/index.html", context)


def breeds_list_view(request):
    context = {
        'objects_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, "dogs/breeds.html", context)


def breeds_dogs_list_view(request, pk: int):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(breed_id=pk),
        'title': f'Cобаки породы - {breed_item.name}',
        'breed_pk': breed_item.pk,
    }
    return render(request, 'dogs/dogs.html', context)


class DogListView(ListView):
    model = Dog
    extra_context = {
        'title': 'Питомник - Все наши породы'

    }
    template_name = 'dogs/dogs.html'

# def dogs_list_view(request):
#     context = {
#         'objects_list': Dog.objects.all(),
#         'title': 'Питомник - Все наши собаки'
#     }
#     return render(request, 'dogs/dogs.html', context)


# def dog_create_view(request):
#     if request.method == "POST":
#         form = DogForm(request.POST, request.FILES)
#         if form.is_valid():
#             dog_object = form.save()
#             dog_object.owner = request.user
#             dog_object.save()
#             return HttpResponseRedirect(reverse('dogs:dogs_list'))
#     return render(request,'dogs/create.html',{'form':DogForm()})
class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm
    template_name = 'dogs/create_update.html'
    extra_context = {
        'title':'Добавить собаку'
    }
    success_url = reverse_lazy('dogs:dogs_list')


class DogDetailView(DetailView):
    model = Dog
    template_name = 'dogs/detail.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dog_object = self.get_object()
        context['title'] = f'вы выбрали {dog_object.name}, Порода {dog_object.breed.name}'
        return context


# def dog_detail_view(request,pk):
#     dog_object = Dog.objects.get(pk=pk)
#     context = {
#         'object': dog_object,
#         'title': f'вы выбрали {dog_object.name}, Порода {dog_object.breed.name}'
#     }
#     return render(request,'dogs/detail.html',context)


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm
    template_name = 'dogs/create_update.html'
    extra_context = {
        'title': f'Изменить собаку'
    }
    def get_success_url(self):
        return reverse('dogs:dog_detail',args=[self.kwargs.get('pk')])
# def dog_update_view(request,pk):
#     dog_object = get_object_or_404(Dog,pk=pk)
#     if request.method =="POST":
#         form = DogForm(request.POST, request.FILES, instance=dog_object)
#         if form.is_valid():
#             dog_object = form.save()
#             dog_object.save()
#             return HttpResponseRedirect(reverse('dogs:dog_detail', args={pk: pk}))
#     context = {
#         'objects_list': dog_object,
#         'form': DogForm(instance=dog_object)
#     }
#     return render(request,'dogs/update.html',context)


def dog_delete_view(request,pk):
    dog_object = get_object_or_404(Dog, pk =pk)
    if request.method ==  'POST':
        dog_object.delete()
        return HttpResponseRedirect(reverse('dogs:dogs_list'))
    context = {
        'object': dog_object}
    return render(request,'dogs/delete.html',context)