from django.db import models

from dashboard.models import Candidate


class Vote(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=255)
    roll = models.CharField(max_length=100)
    president = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True, related_name='vote_count')
    vice_president = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True, related_name='vc_count')
    general_secretary = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True, related_name='gen_sec_count')
    treasurer = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True, related_name='treasurer_count')

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
