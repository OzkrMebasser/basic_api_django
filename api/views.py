from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Tour
from base.models import User
from .serializers import TourSerializer
from .serializers import UserSerializer

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

@api_view(['GET'])
def get_users(request):
    Users = User.objects.all()
    serializer = UserSerializer(Users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
