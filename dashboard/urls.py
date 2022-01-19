from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('candidate/', CandidateView.as_view(), name='candidate'),
    path('candidate/<int:id>/', CandidateUpdate.as_view(), name='update'),
    path('candidate/<int:id>/delete/', CandidateDeleteView.as_view(), name='delete'),
]
