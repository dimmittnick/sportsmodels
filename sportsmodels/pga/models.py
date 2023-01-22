from django.db import models
from datetime import *


class PgaPreds(models.Model):
    golfer = models.CharField(('Golfer'), max_length=64)
    position = models.IntegerField(('Ranking'))
