from lib2to3.fixes.fix_input import context

from PIL.ImageFilter import DETAIL
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  Http404, HttpResponseForbidden

from django.forms import inlineformset_factory

from django.urls import reverse, reverse_lazy
from dogs.models import Breed, Dog, DogParent
from dogs.forms import DogForm, DogParentForm, DogAdminForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from dogs.servises import send_views_mail
from users.models import UserRoles


# Create your views here
def index(request):
    context = {
        'object_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, "dogs/index.html", context)


class DogBreedListView(LoginRequiredMixin,ListView):
    model = Dog
    template_name = 'dogs/dogs.html'
    extra_context = {
        'title': 'Cобаки выбранной породы'
    }
    def get_queryset(self):
        queryset = super().get_queryset().filter(breed_id= self.kwargs.get('pk'))
        return queryset


class BreedListView(LoginRequiredMixin,ListView):
    model = Breed
    extra_context = {
        'title':"Все наши породы"
    }
    template_name = 'dogs/breeds.html'


class DogListView(ListView):
    model = Dog
    extra_context = {
        'title': 'Питомник - Все наши породы'
    }
    template_name = 'dogs/dogs.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active = True)
        return queryset

class DogDeactivatedListView(LoginRequiredMixin,ListView):
    model = Dog
    extra_context = {
        'title': "Питомник - неактивыне собаки"
    }
    template_name = "dogs/dogs.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            queryset = queryset.filter(is_active= False)
        if self.request.user.role == UserRoles.USER:
            queryset = queryset.filter(is_active=False, owner= self.request.user)
        return queryset

class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    template_name = 'dogs/create_update.html'
    extra_context = {
        'title': 'Добавить собаку'
    }
    success_url = reverse_lazy('dogs:dogs_list')

    def form_valid(self, form):
        if self.request.user.role != UserRoles.USER:
            raise  PermissionDenied
        self.object = form.save()
        self.object.owner = self.request.user
        return super().form_valid(form)



class DogDetailView(DetailView):
    model = Dog
    template_name = 'dogs/detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dog_object = self.get_object()
        context['title'] = f'вы выбрали {dog_object.name}, Порода {dog_object.breed.name}'
        dog_object_increase = get_object_or_404(Dog, pk=dog_object.pk)
        if dog_object.owner != self.request.user:
            dog_object_increase.views_count()
        if dog_object.owner:
            dog_object_owner_email = dog_object.owner.email
            if dog_object_increase.views%20 == 0 and dog_object_increase != 0:
                 send_views_mail(dog_object_increase.name,dog_object_owner_email, dog_object_increase.views)

        return context



class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogForm
    template_name = 'dogs/create_update.html'
    extra_context = {
        'title': f'Изменить собаку'
    }

    def get_success_url(self):
        return reverse('dogs:dog_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # if self.object.owner != self.request.user and not self.request.user.is_staff:
        if self.object.owner != self.request.user and self.request.user.role != UserRoles.ADMIN:
            raise PermissionDenied()
        return self.object

    def get_form_class(self):
        dog_forms = {
            'admin':DogAdminForm,
            'moderator':DogForm,
            'user':DogForm,
        }
        user_role =self.request.user_role
        dog_form_class = dog_forms[user_role]
        return dog_form_class

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        DogParentFormset = inlineformset_factory(Dog, DogParent, form=DogParentForm, extra=1)
        if self.request.method == 'POST':
            formset = DogParentFormset(self.request.POST, instance=self.object)
        else:
            formset = DogParentFormset( instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class DogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Dog
    template_name = 'dogs/delete.html'
    extra_context = {
        'title': "удалить собаку"
    }
    success_url = reverse_lazy("dogs:dogs_list")
    permission_required = 'dogs.delete_dog'
    permission_denied_message = "Не достаточно прав"

def toggle_activity(request, pk):
    dog_item = get_object_or_404(Dog,pk=pk)
    if dog_item.is_active:
        dog_item.is_active = False
    else:
        dog_item.is_active = True
    dog_item.save()
    return redirect(reverse("dogs:dogs_list"))