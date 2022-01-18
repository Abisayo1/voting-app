from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('candidate/', CandidateView.as_view(), name='candidate')
]
