from .models import Stock
from django.db import transaction

@transaction.atomic # Si algo falla a la mitad, se cancela todo (no hay datos corruptos)
def reduce_stock(medicine_id: str, quantity_to_reduce: int):
    # Buscamos lotes de esta medicina que tengan stock mayor a 0
    stocks = Stock.objects.filter(medicine_id=medicine_id, quantity__gt=0).order_by('id')
    
    remaining = quantity_to_reduce
    
    for stock in stocks:
        if remaining <= 0:
            break
            
        if stock.quantity >= remaining:
            stock.quantity -= remaining
            stock.save()
            remaining = 0
        else:
            remaining -= stock.quantity
            stock.quantity = 0
            stock.save()
            
    if remaining > 0:
        # Si revisamos todos los lotes y aún falta por descontar...
        raise ValueError("No hay suficiente stock disponible en inventario para cubrir la venta.")
    
    return True