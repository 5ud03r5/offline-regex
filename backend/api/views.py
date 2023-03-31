from .serializers import RegexSerializer, TagsSerializer
from regex.models import Regex, Tag
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class RegexViewSet(ListCreateAPIView):
    queryset = Regex.objects.all()
    serializer_class = RegexSerializer
    
    def create(self, request, *args, **kwargs):      
        tags = request.data.pop('tags')
        serializer = self.get_serializer(data=request.data)   
        serializer.is_valid()   
        print(serializer.errors)
        self.perform_create(serializer, tags)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 

    def perform_create(self, serializer, tags):
        serializer.save(tags=tags)

class TagsViewSet(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer