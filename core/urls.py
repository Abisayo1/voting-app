from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('home/', IndexView.as_view(), name="index"),
    path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
