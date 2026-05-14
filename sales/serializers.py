from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    # Traemos el nombre de la medicina para que el frontend lo lea fácil
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'