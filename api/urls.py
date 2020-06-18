from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list/', views.task_list, name='tasks'),
    path('task-detail/<str:pk>/', views.task_detail, name='task-detail'),
]
