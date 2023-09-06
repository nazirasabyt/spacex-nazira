from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Link
from .models import Advantage
from .serializers import LinkSerializer
from .serializers import AdvSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(requests):
    return Response('hello')


@api_view(['GET'])
def getLinks(requests):
    links= Link.objects.all()
    serializer=LinkSerializer(links, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAdvantages(requests):
    adv= Advantage.objects.all()
    serializer=AdvSerializer(adv, many=True)
    return Response(serializer.data)