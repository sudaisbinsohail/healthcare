from django.http import JsonResponse

def success_response(status='success', message=None, data=None):
    response = {'status': status}
    if message:
        response['message'] = message
    if data:
        response['data'] = data
    return response




