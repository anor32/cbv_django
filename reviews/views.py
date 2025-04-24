

from django.shortcuts import render
from  django.http import  HttpResponseForbidden
from django.shortcuts import reverse,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions  import PermissionDenied
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from  redis.commands.search.querystring import  querystring

from reviews.forms import ReviewForm
from reviews.models import Review
from reviews.utils import slug_generator
from users.models import UserRoles


class ReviewListView(ListView):
    model = Review
    extra_context = {
        'title': 'Все отзывы'
    }
    template_name = 'reviews.html'
    paginate_by = 2
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_review=True)
        return queryset





class ReviewDeactivatedListView(ListView):
    model = Review
    extra_context = {
        'title': 'все  Неактивные отзывы'
    }
    template_name = 'reviews.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_review=False)
        return queryset


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create-update.html'
    extra_context = {
        'title': 'Написать отзыв'
    }

    def form_valid(self, form):
        if self.request.user.role not in [UserRoles.USER,UserRoles.ADMIN]:
            return HttpResponseForbidden
        self.object = form.save()
        print(self.object.slug)
        if self.object.slug == 'temp_slug':
            self.object.slug = slug_generator()
            print(self.object.slug)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = 'detail.html'
    extra_context = {
        "title": "Просмотр отзыва"
    }
class ReviewUpdateView(LoginRequiredMixin,UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create-update.html'
    extra_context = {
        "title": 'Изменить отзыв'
    }

    def get_success_url(self):
        return reverse('reviews:review_detail', args=[self.kwargs.get('slug')])

    def get_object(self, queryset= None):
        self.object = super().get_object(queryset= queryset)
        if self.object.author != self.request.user and self.request.user not in (UserRoles.ADMIN, UserRoles.MODERATOR):
            raise PermissionDenied()
        return self.object

class ReviewDeleteView(LoginRequiredMixin,DeleteView):
    model = Review
    template_name = 'delete.html'
    permission_required = 'reviews.delete_review'

    def get_success_url(self):
        return reverse('reviews:reviews_list')


def review_toggle_activity(request, slug):
    review_item = get_object_or_404(Review,slug=slug)
    if review_item.sign_of_review:
        review_item.sign_of_review = False
        review_item.save()
        return redirect(reverse('reviews:review_deactivated'))
    else:
        review_item.sign_of_review = True
        review_item.save()
        return redirect(reverse('reviews:reviews_list'))


