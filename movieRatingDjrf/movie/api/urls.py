from django.urls import path
from .import views


urlpatterns = [
    path('',views.movieList,name='movieList'),
    path('<int:pk>',views.movie,name='movie'),
    
]
