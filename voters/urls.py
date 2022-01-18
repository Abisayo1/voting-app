from django.urls import path
from .views import *

app_name = 'voter'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vote/', VoteView.as_view(), name='vote'),
    path('update/', CandidateUpdate.as_view(), name='update')
]
