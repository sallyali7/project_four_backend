from django.urls import path
from .views import BlogsListView, BlogsDetailView

urlpatterns = [
    path('', BlogsListView.as_view()),
    path('<int:pk>', BlogsDetailView.as_view()),
]