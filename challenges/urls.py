from django.urls import path
from .views import challenge_list

urlpatterns = [
    path('challenges/', challenge_list, name='challenge-list'),
]