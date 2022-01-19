from django.shortcuts import render
from django.views import View
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
        return render(request, "polls/pollResult.html", context)
