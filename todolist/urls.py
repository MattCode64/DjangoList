from django.urls import path
from .views import CollectionList, TaskList, CollectionDetail, TaskDetail

urlpatterns = [
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('collections/<int:collection_pk>/', CollectionDetail.as_view(), name='collection-detail'),
    path('tasks/<int:task_pk>/', TaskDetail.as_view(), name='task-detail'),
]