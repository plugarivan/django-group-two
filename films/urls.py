from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmsView.as_view(), name='home'),
    path('<slug:slug>/', views.FilmDetail.as_view(), name='film_detail'),
    path('reviews/<int:pk>/', views.AddReview.as_view(), name='add_review')
]