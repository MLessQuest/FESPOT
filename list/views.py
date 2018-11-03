from rest_framework import viewsets
from .serializers import FestivalSerializer, ContestSerializer
from .models import Festival, Contest
from django.shortcuts import render


class FestivalViewSet(viewsets.ModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
	
def findex(request):
    festivals = Festival.objects.order_by('ftitle')
    return render(request, 'list/festival.html', {'festivals': festivals})

def cindex(request):
    contests = Contest.objects.order_by('ctitle')
    return render(request, 'list/contest.html', {'contests': contests})