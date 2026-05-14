from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importar las vistas
from catalog.views import MedicineViewSet
from inventory.views import StockViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from sales.views import SaleViewSet

# Enrutador automático de DRF
router = DefaultRouter()
router.register(r'medicines', MedicineViewSet, basename='medicine')
router.register(r'stock', StockViewSet, basename='stock')
router.register(r'sales', SaleViewSet, basename='sale') # <-- Línea agregada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    
    # Endpoints de la documentación
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]