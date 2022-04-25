from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Tour
from .serializers import TourSerializer

@api_view(['GET'])
def get_data(request):
    Tours = Tour.objects.all()
    serializer = TourSerializer(Tours, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_tour(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)