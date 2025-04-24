from django.urls import path
from django.views.generic import DetailView

from reviews.apps import ReviewsConfig
from reviews.models import Review
from reviews.views import ReviewDeactivatedListView, ReviewListView, ReviewDetailView, ReviewUpdateView, \
    ReviewDeleteView, review_toggle_activity, ReviewCreateView


app_name  = ReviewsConfig.name

urlpatterns = [
    path('',ReviewListView.as_view(), name= 'reviews_list'),
    path('deactivated/',ReviewDeactivatedListView.as_view(), name= 'review_deactivated'),
    path('review/create/',ReviewCreateView.as_view(), name= 'review_create'),
    path('review/detail/<slug:slug>/',ReviewDetailView.as_view(), name= 'review_detail'),
    path('review/update/<slug:slug>/',ReviewUpdateView.as_view(), name= 'review_update'),
    path('review/delete/<slug:slug>/',ReviewDeleteView.as_view(), name= 'review_delete'),
    path('review/toggle/<slug:slug>/',review_toggle_activity, name= 'review_toggle_activity'),

]