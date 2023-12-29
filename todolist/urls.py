from django.urls import path
from .views import *

urlpatterns = [
    path('collections/', CollectionList.as_view(), name='collection-list'),
    # For displaying all collections (list, create)
    path('collections/<int:collection_pk>/', CollectionDetail.as_view(), name='collection-detail'),
    # For displaying a collection detail (update, delete)
    path('collections/<int:collection_pk>/tasks/', TasksList.as_view(), name='tasks-list'),
    # For displaying all tasks of a collection (list, create)
    path('collections/<int:collection_pk>/tasks/<int:task_pk>/', TaskDetail.as_view(), name='task-detail'),
    # For displaying a task detail (update, delete)
]
