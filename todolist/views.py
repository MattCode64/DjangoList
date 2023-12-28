from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Collection, Task
from .serializers import CollectionSerializer, TaskSerializer


# Create your views here.

class CollectionList(generics.ListCreateAPIView):
    # Display all collections
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class TaskList(generics.ListAPIView):
    # Display all tasks
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CollectionDetail(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_object(self):
        collection_pk = self.kwargs["collection_pk"]
        return Collection.objects.get(pk=collection_pk)

    def get(self, request, *args, **kwargs):
        try:
            collection = self.get_object()
            serializer = CollectionSerializer(collection)
            return Response(serializer.data)
        except Collection.DoesNotExist:
            return Response({"CollectionDetail": "Not found or does not exist."}, status=status.HTTP_404_NOT_FOUND)


class TaskDetail(generics.RetrieveAPIView):
    serializer_class = TaskSerializer

    def get_object(self):
        task_pk = self.kwargs["task_pk"]
        return Task.objects.get(pk=task_pk)

    def get(self, request, *args, **kwargs):
        try:
            task = self.get_object()
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"TaskDetail": "Not found or does not exist."}, status=status.HTTP_404_NOT_FOUND)
