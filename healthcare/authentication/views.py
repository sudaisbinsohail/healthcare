from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterUserSerializer , LoginSerializer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken





@api_view(['POST'])
def register(request):
    try:
        serializer = RegisterUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status.HTTP_201_CREATED)
        return Response({'error':serializer.errors },status.HTTP_404_NOT_FOUND)
    except Exception as e:
         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
def login(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token), 'user':serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    


@api_view(['POST'])
def refreshToken(request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)  
        try:
            refresh = RefreshToken(refresh_token)
            user =  refresh.payload.get('user_id')
            user = User.objects.get(pk=user)
            new_refresh_token = str(RefreshToken.for_user(user))
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({'access': str(refresh.access_token) , 'refresh':str(new_refresh_token)}, status=status.HTTP_200_OK)
    
    
    
    


