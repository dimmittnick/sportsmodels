from django.db import models


class HitterPreds(models.Model):
    name = models.CharField(('Name'), max_length=64)
    pa = models.FloatField(('pa_pred'))
    runs = models.FloatField(('r'))
    homerun = models.FloatField(('hr'))
    rbi = models.FloatField(('rbi'))
    sb = models.FloatField(('sb'))
    obp = models.FloatField(('obp'))

class PitcherPreds(models.Model):
    name = models.CharField(('Name'), max_length=64)
    wins = models.FloatField(('W'))
    so = models.FloatField(('SO'))
    era = models.FloatField(('ERA'))
    whip = models.FloatField(('WHIP'))
    svh = models.FloatField(('SVH'))