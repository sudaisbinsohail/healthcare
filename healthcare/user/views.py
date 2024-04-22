from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from healthcare.helper.responses import success_response
from healthcare.authentication.models import User
from healthcare.authentication.serializers import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_patient(request):
            users = User.objects.filter(user_type='patient').order_by('-created_at')
            allergies = UserSerializer(users,many=True)
            return Response(success_response(message="Users Fetch Successfully", data=allergies.data), status=status.HTTP_200_OK)

