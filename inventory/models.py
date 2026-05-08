import uuid
from django.db import models

class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medicine_id = models.UUIDField()  # La clave para que tus compañeros no sufran luego
    batch_number = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Lote {self.batch_number} - Qty: {self.quantity}"