from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import BlogSerializer
from .models import Blogs

# Create your views here.

class BlogsListView(ListCreateAPIView):

    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class BlogsDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer