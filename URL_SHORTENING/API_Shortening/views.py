from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from .models import URL
from .serializers import URLSerializer, RetrieveOriginalURLSerializer
from rest_framework.response import Response
import re
import string
import secrets

@api_view(['POST'])
def CreateShortendedURL(request):
    data = request.data
    original_url = data.get('url')

    if not original_url:
        return Response({"mssg": "URL is required"}, status=400)

    
    existing_entry = URL.objects.filter(url=original_url).first()
    if existing_entry:
        serializer = RetrieveOriginalURLSerializer(existing_entry)
        return Response(serializer.data)

    while True:
        shortened_url = generateShortenedURL()
        if not URL.objects.filter(shortcode=shortened_url).exists():
            break

    
    obj = URL.objects.create(url=original_url, shortcode=shortened_url)
    serializer = RetrieveOriginalURLSerializer(obj)
    
    return Response(serializer.data)




class RetrieveUpdateDestroyURLView(generics.RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    lookup_field = "shortcode"

    def get_serializer_class(self):
        
        if self.request.method == "GET":
            return RetrieveOriginalURLSerializer
        return URLSerializer 

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.increment_access_count()  
        return  Response({"url": obj.url,
    "shortcode": obj.shortcode,
    "createdAt": obj.createdAt,
    "updatedAt": obj.updatedAt,})

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.url = request.data.get('url', obj.url)
        obj.save()
        return Response({"url": obj.url,
    "shortcode": obj.shortcode,
    "createdAt": obj.createdAt,
    "updatedAt": obj.updatedAt,})

class RetrieveStatView(generics.RetrieveAPIView):
    serializer_class = RetrieveOriginalURLSerializer
    queryset = URL.objects.all()
    lookup_field = "shortcode"
    
def generateShortenedURL(length=6):
    
    characters = string.ascii_letters + string.digits

    return "".join(secrets.choice(characters) for _ in range(length))