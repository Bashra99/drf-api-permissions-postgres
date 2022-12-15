from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from .models import AOT
from .models import Titan   
from .serializers import AOTSerializer
from .serializers import TitanSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class AOTListView(ListAPIView):
    queryset = AOT.objects.all()
    serializer_class= AOTSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]



class AOTDetailView(RetrieveUpdateDestroyAPIView):
    queryset = AOT.objects.all()
    serializer_class= AOTSerializer
    permission_classes=[IsOwnerOrReadOnly]

class TitanListView(ListAPIView):
    queryset = Titan.objects.all()
    serializer_class= TitanSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]


class TitanDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Titan.objects.all()
    serializer_class= TitanSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]





