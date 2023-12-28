from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Collection, Task


# Create your tests here.

class CollectionAPITests(APITestCase):
    def setUp(self):
        self.collection = Collection.objects.create(title="Test Collection")

    def test_list_collections(self):
        url = reverse('collection-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_collection_success(self):
        url = reverse('collection-detail', args=[self.collection.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_collection_not_found(self):
        url = reverse('collection-detail', args=[999])  # Un ID qui n'existe pas
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TaskAPITests(APITestCase):
    def setUp(self):
        self.collection = Collection.objects.create(title="Test Collection")
        self.task = Task.objects.create(title="Test Task", collection=self.collection)

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_task_success(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_task_not_found(self):
        url = reverse('task-detail', args=[999])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
