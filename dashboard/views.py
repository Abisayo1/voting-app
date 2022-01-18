from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from core.models import Profile
from .models import *


class IndexView(View):
    def get(self, request):
        user = User.objects.filter(is_staff=True, is_superuser=False)
        context = {
            "user": user,
        }
        return render(request, "dashboard/index.html", context)


class CandidateView(View):
    def get(self, request):
        candidates = Candidate.objects.all()
        context = {
            "candidates": candidates
        }
        return render(request, "dashboard/candidates.html", context)

    def post(self, request):
        first_name = request.POST.get('first_name',)
        last_name = request.POST.get('last_name',)
        position = request.POST.get('position',)

        if first_name == '' and last_name == '':
            messages.error(request, "Name has not been added")
            return redirect("dashboard:candidate")

        candidate = Candidate.objects.create(first_name=first_name, last_name=last_name, position=position)
        messages.success(request, "Candidate added successfully")
        candidate.save()

        return redirect("dashboard:candidate")


class ProfileView(View):
    def get(self, request, slug):
        pass
