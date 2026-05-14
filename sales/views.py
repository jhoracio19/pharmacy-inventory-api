from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

# Importamos tu modelo y tu convertidor
from .models import Sale
from .serializers import SaleSerializer

# ==========================================
# 1. ENDPOINT DE VENTAS (Para el Microservicio)
# ==========================================
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-created_at')
    serializer_class = SaleSerializer


# ==========================================
# 2. ENDPOINT DE LOGIN (Para el Frontend)
# ==========================================
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        # Genera o recupera el token del usuario
        token, _ = Token.objects.get_or_create(user=user)
        # Si es "Staff" en Django, es Admin. Si no, es Cajero.
        role = 'admin' if user.is_staff else 'cajero'
        
        return Response({
            'token': token.key,
            'user': {
                'name': user.username,
                'role': role
            }
        })
    return Response({'error': 'Credenciales inválidas'}, status=400)