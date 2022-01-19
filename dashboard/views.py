from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Profile
from .models import *


class IndexView(LoginRequiredMixin, View):
    login_url = 'core:register'

    def get(self, request):
        user = User.objects.filter(is_staff=True, is_superuser=False)
        context = {
            "user": user,
        }
        return render(request, "dashboard/index.html", context)


class CandidateView(LoginRequiredMixin, View):
    login_url = 'core:register'

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
            return redirect("dashboard:candidate")

        candidate = Candidate.objects.create(first_name=first_name, last_name=last_name, position=position)
        candidate.save()

        return redirect("dashboard:candidate")


class CandidateUpdate(LoginRequiredMixin, View):
    login_url = 'core:register'

    def get(self, request, id):
        candidate = Candidate.objects.get(id=id)
        context = {
            'candidate': candidate
        }
        return render(request, "dashboard/update.html", context)

    def post(self, request, id):
        first_name = request.POST.get('first_name', )
        last_name = request.POST.get('last_name', )
        position = request.POST.get('position', )

        candidate = Candidate.objects.get(id=id)

        candidate.first_name = first_name
        candidate.last_name = last_name
        candidate.position = position
        candidate.save()
        return redirect("dashboard:candidate")


class CandidateDeleteView(LoginRequiredMixin, View):
    login_url = 'core:register'

    def get(self, request, id):
        candidate = Candidate.objects.get(id=id)
        candidate.delete()
        return redirect("dashboard:candidate")


class ProfileView(View):
    def get(self, request, slug):
        pass
