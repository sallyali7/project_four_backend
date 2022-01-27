from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Jobs
from .serializers import JobSerializer



class JobsListView(ListCreateAPIView):

    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    # permission_classes = (IsAuthenticated)

class JobsDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    # permission_classes = (IsAuthenticated)






# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Jobs
# from .serializers import JobSerializer

# class JobsListView(APIView):

#     def get(self, _request):
#         jobs = Jobs.objects.all()
#         serialized_jobs = JobSerializer(jobs, many=True)
#         return Response(serialized_jobs.data, status=status.HTTP_200_OK)

# class JobsDetailView(APIView):

#     def get(self, _request, pk):
#         serialized_jobs = JobSerializer(Jobs)
#         return Response(serialized_jobs.data, status=status.HTTP_200_OK)