from django.urls import path
from .views import JobsListView, JobsDetailView


urlpatterns = [
    path('', JobsListView.as_view()),
    path('<int:pk>/', JobsDetailView.as_view()),
]