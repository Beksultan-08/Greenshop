from rest_framework import generics
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView

from product.models import Plant
from product.serializer import PlantSerializer


class PlantListAPIView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantCreateAPIView(generics.CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantUpdateAPIView(generics.UpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'id'

class PlantDeleteAPIView(generics.DestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'id'


class PlantDetailAPIView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'id'


class PlantDetailDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'id'


class PlantDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'id'


class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
