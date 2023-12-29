from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Collection, Task


# Create your tests here.

def test_success(test_name):
    # Print the test name in yellow
    print("\033[93m" + " ~~~ TEST " + test_name + " SUCCESS ~~~ " + "\033[0m")


class CollectionAPITests(APITestCase):
    def setUp(self):
        self.collection = Collection.objects.create(title="Test Collection")

    def test_create_collection(self):
        url = reverse('collection-list')
        data = {'title': 'New Test Collection Created'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        test_success("COLLECTION CREATE")

    def test_list_collection(self):
        url = reverse('collection-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_success("COLLECTION LIST")

    def test_destroy_collection(self):
        url = reverse('collection-detail', kwargs={'collection_pk': self.collection.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        test_success("COLLECTION DELETE")

    def test_retrieve_collection(self):
        url = reverse('collection-detail', kwargs={'collection_pk': self.collection.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_success("COLLECTION RETRIEVE")

    def test_update_collection(self):
        url = reverse('collection-detail', kwargs={'collection_pk': self.collection.pk})
        data = {'title': 'Test Collection Updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_success("COLLECTION UPDATE")


class TaskAPITests(APITestCase):
    def setUp(self):
        self.collection = Collection.objects.create(title="Test Collection")
        self.task = Task.objects.create(title="Test Task", collection=self.collection)

    def test_create_task(self):
        url = reverse('tasks-list', kwargs={'collection_pk': self.collection.pk})
        data = {'title': 'New Test Task Created', 'collection': self.collection.pk}
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        test_success("TASK CREATE")

    def test_list_task(self):
        url = reverse('tasks-list', kwargs={'collection_pk': self.collection.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_success("TASK LIST")

    def test_destroy_task(self):
        url = reverse('task-detail', kwargs={'task_pk': self.task.pk, 'collection_pk': self.collection.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        test_success("TASK DELETE")

    def test_retrieve_task(self):
        url = reverse('task-detail', kwargs={'task_pk': self.task.pk, 'collection_pk': self.collection.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_success("TASK RETRIEVE")

    def test_update_task(self):
        url = reverse('task-detail', kwargs={'task_pk': self.task.pk, 'collection_pk': self.collection.pk})
        data = {'title': 'Test Task Updated', 'collection': self.collection.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_success("TASK UPDATE")
