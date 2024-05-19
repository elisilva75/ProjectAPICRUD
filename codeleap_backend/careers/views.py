from rest_framework import generics
from .models import CareerPost
from .serializers import CareerPostSerializer

class CareerPostListCreateView(generics.ListCreateAPIView):
    queryset = CareerPost.objects.all()
    serializer_class = CareerPostSerializer

class CareerPostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CareerPost.objects.all()
    serializer_class = CareerPostSerializer
