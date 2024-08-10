from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
