from .models import University
from .serializers import UniversitySerializer
from rest_framework import generics

class UniversityList(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

