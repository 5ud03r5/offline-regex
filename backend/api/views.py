from .serializers import RegexSerializer, TagsSerializer
from regex.models import Regex, Tag
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response

from django.db.models.query import QuerySet


class RegexViewSet(ListCreateAPIView):
    queryset = Regex.objects.all()
    serializer_class = RegexSerializer
    
    def create(self, request, *args, **kwargs):      
        tags = request.data.pop('tags')
        serializer = self.get_serializer(data=request.data)   
        serializer.is_valid(raise_exception=True)   
        self.perform_create(serializer, tags)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 

    def perform_create(self, serializer, tags):
        serializer.save(tags=tags)

    def list(self, request, *args, **kwargs):
        tags = request.GET.get('tags')
        if tags is not None:
            tags = tags.split(',')
            queryset = Regex.objects.filter(tags__in=tags).distinct()
            for tag in tags:
                queryset = queryset.filter(tags__id=tag)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SingleRegexViewSet(ListAPIView):
    serializer_class = RegexSerializer

    def get_queryset(self, pk):
        queryset = Regex.objects.get(id=pk)
        return queryset

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = self.filter_queryset(self.get_queryset(pk))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

class TagsViewSet(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer