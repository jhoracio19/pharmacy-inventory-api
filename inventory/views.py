from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer
from .services import reduce_stock # Importamos nuestra lógica

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # Esto crea automáticamente el endpoint: POST /api/v1/stock/reduce_stock/
    @action(detail=False, methods=['post'])
    def reduce_stock(self, request):
        medicine_id = request.data.get('medicine_id')
        quantity = request.data.get('quantity', 0)

        # Validación básica
        if not medicine_id or int(quantity) <= 0:
            return Response(
                {"error": "Faltan datos: se requiere 'medicine_id' y un 'quantity' mayor a 0"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Llamamos a nuestra capa de servicios aislada
            reduce_stock(medicine_id, int(quantity))
            return Response({"message": "Stock descontado exitosamente"}, status=status.HTTP_200_OK)
            
        except ValueError as e:
            # Si el servicio lanza nuestro error de "No hay stock"
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)