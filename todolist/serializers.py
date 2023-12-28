from rest_framework import serializers
from .models import Task, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title']


class CollectionDeleteSerializer(serializers.ModelSerializer):
    # I want to delete with the title or id
    class Meta:
        model = Collection
        fields = ['title']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['id', 'title', 'slug', 'description', 'completed', 'created', 'collection']
