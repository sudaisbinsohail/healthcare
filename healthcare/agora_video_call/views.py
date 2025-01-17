from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
import jwt  
from datetime import datetime, timedelta
import uuid 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import pusher
import string
import random
from agora_token_builder import RtcTokenBuilder

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_agora_token(request):
  
    user = request.user 
    sender_id= user.id 
    receiver_id = request.data.get('receiver_id', None)
    agora_uid =  request.data.get('agora_uid', None)
  

    if not sender_id or not receiver_id:
        sender_id =1
        receiver_id=2
        # return Response({'error': 'Please provide sender and receiver id'}, status=status.HTTP_400_BAD_REQUEST)

    if not agora_uid:
        agora_uid = 0 

    # channel_name = f'call-{uuid.uuid4()}-{sender_id}-{receiver_id}' 
    channel_name = generate_random_string(12)

    AGORA_APP_ID = 'dace37e811464511a92ce19e225e66fa'
    AGORA_APP_CERTIFICATE = '49a559abc1ff4cc0a6cec32d508fb081'
    
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    # token = jwt.encode({
    #     'app_id': AGORA_APP_ID,
    #     'uid': agora_uid,
    #     'channel_name': channel_name,
    #     'exp': expiration_time
    # }, AGORA_APP_CERTIFICATE, algorithm='HS256')

    token = RtcTokenBuilder.buildTokenWithAccount(
        AGORA_APP_ID,
        AGORA_APP_CERTIFICATE,
        channel_name,
        account = 'user_account',
        role =0 ,
        privilegeExpiredTs = 3600 )

      
    # pusher_client = pusher.Pusher(
    #    app_id = "1790808",
    #    key = "7eea74474e4ac958eed6",
    #    secret = "5b301ddeca15cfb9abaf",
    #    cluster = "ap2",
    #    ssl=True
    # )

    
    # pusher_client.trigger('video-call', 'start-call', {
    #     'sender_id': sender_id,
    #     'receiver_id': receiver_id,
    #     'channel_name': channel_name,
    #     'token': token
    # })


    return Response({'token': token, 'channel_name': channel_name, 'app_id':AGORA_APP_ID}, status=status.HTTP_200_OK)



#helper to generate random string
def generate_random_string(length):
    letters_and_digits = string.ascii_letters
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
