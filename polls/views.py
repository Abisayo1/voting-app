from django.shortcuts import render
from django.views import View

from dashboard.models import Candidate


class IndexView(View):
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
