from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import HealthProfile
from .serializers import HealthProfileSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_health_profile(request):
    if request.method == 'POST':
        user = request.user 
        request.data['user'] = user.id 
        serializer = HealthProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
