from django.shortcuts import render
from .models import Tutorial
from .serializers import TutorialSeralizer
from rest_framework.viewsets import ModelViewSet


class TutorialView(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSeralizer
    
