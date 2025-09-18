from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import User

@api_view(['POST'])
@csrf_exempt
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'success': True,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'role': user.role,
                    'company_name': user.company_name
                }
            })
        return Response({'success': False, 'error': 'Invalid credentials'})
    except Exception as e:
        return Response({'success': False, 'error': str(e)})

@api_view(['GET'])
def dashboard_api(request):
    return Response({
        'total_users': User.objects.count(),
        'message': 'API working!'
    })