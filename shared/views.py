from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from shared.models import Feature
from shared.serializers import FeatureSerializer

# Create your views here.

def index(request):
    return HttpResponse("<p>Hello, Everyone</p>")

class FeatureListAPIView(ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    
class FeatureRetrieveAPIView(RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

