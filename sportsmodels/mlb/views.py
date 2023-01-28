from django.shortcuts import render
from .models import HitterPreds, PitcherPreds

def index(request):
    hitpreds = HitterPreds.objects.all()
    pitchpreds = PitcherPreds.objects.all()
    hit_preds = sorted(hitpreds, key=lambda x:x.homerun, reverse=True)
    pitch_preds = sorted(pitchpreds, key=lambda x:x.era, reverse=False)
    context = {'hitspreds':hitpreds,
               'pitchpreds':pitchpreds,
               'hit_preds':hit_preds,
               'pitch_preds':pitch_preds}
    return render(request, "mlb/index.html", context)