from django.db import models
from datetime import *


class NhlPreds(models.Model):
    date = models.CharField(('Date'), max_length=64, default=datetime.today().strftime("%Y-%m-%d"))
    skater = models.CharField(('Skater'), max_length=64)
    team = models.CharField(('Team'), max_length=3)
    opponent = models.CharField(('Opponent'), max_length=3)
    prediction = models.FloatField(("Prediction"))


