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


class TasksList(generics.ListCreateAPIView):
    """
    Cette classe permet de lister toutes les tâches d'une collection et d'ajouter
    tâches à la collection.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        collection_id = self.kwargs["collection_pk"]
        return Task.objects.filter(collection=collection_id)

    def list(self, request, *args, **kwargs):
        """
        Je redéfinis list méthode parce que je veux afficher les tâches d'une collection avec leur collection.
        Mettre en commentaire la méthode list pour ne pas renvoyer/afficher la collection.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            # Récupérer la collection
            collection_id = self.kwargs["collection_pk"]
            collection = Collection.objects.get(pk=collection_id)
            # Récupérer les tâches de la collection
            tasks = Task.objects.filter(collection=collection_id)
            # Sérialiser la collection
            collection_serializer = CollectionSerializer(collection)
            # Sérialiser les tâches
            tasks_serializer = TaskSerializer(tasks, many=True)
            # Retourner la réponse
            return Response({"collection": collection_serializer.data, "tasks": tasks_serializer.data})

        except Collection.DoesNotExist:
            return Response({"TasksListError": "Not found or does not exist."}, status=status.HTTP_404_NOT_FOUND)

        except Task.DoesNotExist:
            return Response({"TasksListError": "Not found or does not exist."}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        collection_id = self.kwargs["collection_pk"]

        try:
            collection = Collection.objects.get(pk=collection_id)
            serializer.save(collection=collection)
        except Collection.DoesNotExist:
            return Response({"TasksListError": "Collection does not found."}, status=status.HTTP_404_NOT_FOUND)


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_object(self):
        collection_pk = self.kwargs["collection_pk"]
        return Collection.objects.get(pk=collection_pk)

    def retrieve(self, request, *args, **kwargs):
        """
        L'héritage de la classe RetrieveUpdateDestroyAPIView permet de faire un GET, un PUT et un delete.
        J'ai redéfini le get pour qu'il puisse être synchronisé avec les tests unitaires. Sinon il est useless et
        CollectionDetail fonctionne très bien sans.

        :param request:
        :param args:
        :param kwargs:
        :return Response:
        """
        try:
            collection = self.get_object()
            serializer = CollectionSerializer(collection)
            return Response(serializer.data)
        except Collection.DoesNotExist:
            return Response({"CollectionDetail": "Not found or does not exist."}, status=status.HTTP_404_NOT_FOUND)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        task_pk = self.kwargs["task_pk"]
        collection_pk = self.kwargs["collection_pk"]
        return Task.objects.get(pk=task_pk, collection=collection_pk)

    def retrieve(self, request, *args, **kwargs):
        """
        Redéfinition de la méthode retrieve pour qu'elle puisse éviter les erreurs 404.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            task = self.get_object()
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"TaskDetail": "Not found or does not exist."}, status=status.HTTP_404_NOT_FOUND)
