from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from core.models import Profile
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.models import Candidate


class IndexView(LoginRequiredMixin, View):
    login_url = 'core:register'

    def get(self, request):
        president = Candidate.objects.filter(position='President')
        vice_president = Candidate.objects.filter(position='Vice President')
        general_secretary = Candidate.objects.filter(position='Secretary General')
        treasurer = Candidate.objects.filter(position='Treasurer')
        context = {
            'president': president,
            'vice_president': vice_president,
            'general_secretary': general_secretary,
            'treasurer': treasurer,
        }
        return render(request, "voters/ViewCandidates.html", context)


class VoteView(LoginRequiredMixin, View):
    login_url = 'core:register'

    def get(self, request):
        president = Candidate.objects.filter(position='President')
        vice_president = Candidate.objects.filter(position='Vice President')
        general_secretary = Candidate.objects.filter(position='Secretary General')
        treasurer = Candidate.objects.filter(position='Treasurer')

        context = {
            'president': president,
            'vice_president': vice_president,
            'general_secretary': general_secretary,
            'treasurer': treasurer,
        }

        return render(request, "voters/voteCandidate.html", context)

    def post(self, request):
        first_name = request.POST.get('first_name', )
        last_name = request.POST.get('last_name', )
        department = request.POST.get('department', )
        roll = request.POST.get('roll', )
        president = request.POST.get('president', )
        vice_president = request.POST.get('vice_president', )
        general_secretary = request.POST.get('general_secretary', )
        treasurer = request.POST.get('treasurer', )

        vote = Vote.objects.create(
            first_name=first_name,
            last_name=last_name,
            department=department,
            roll=roll,

        )
        vote.save(False)

        if president:
            candidate_president = Candidate.objects.get(first_name=president)
            vote.president = candidate_president
        else:
            pass

        if treasurer:
            candidate_treasurer = Candidate.objects.get(first_name=treasurer)
            vote.treasurer = candidate_treasurer
        else:
            pass

        if vice_president:
            candidate_vp = Candidate.objects.get(first_name=vice_president)
            vote.vice_president = candidate_vp

        if general_secretary:
            candidate_sec_gen = Candidate.objects.get(first_name=general_secretary)
            vote.general_secretary = candidate_sec_gen

        vote.save()
        return redirect('voter:index')


class CandidateUpdate(LoginRequiredMixin, View):
    login_url = 'core:register'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(id=request.user.id)
        context = {
            'profile': profile,
            'user': user
        }
        return render(request, "voters/updateProfile.html", context)

    def post(self, request):
        username = request.POST.get('username', )
        email = request.POST.get('email', )
        phone_number = request.POST.get('phone_number', )
        dob = request.POST.get('dob', )
        gender = request.POST.get('gender', )

        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=request.user)

        if 'profile_image' in request.FILES:
            profile_image = request.FILES['profile_image']
            profile.profile_image = profile_image

        if username:
             user.username = username
             profile.username = username

        if email:
             user.email = email
             profile.email = email

        if phone_number:
            profile.phone_number = phone_number

        if dob:
            profile.dob = dob

        if gender:
            profile.gender = gender

        profile.save()
        user.save()

        return redirect('voter:update')
