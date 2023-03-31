from rest_framework import serializers
from regex.models import Regex, Tag
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RegexSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, required=False)
    class Meta:
        model = Regex
        fields = '__all__'
        
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print(tags_data)
        tags = []
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data)
            tags.append(tag)

        regex = Regex.objects.create(**validated_data)
        regex.tags.set(tags)
        return regex



    
