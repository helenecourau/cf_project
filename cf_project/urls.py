from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api_rest import views

router = routers.DefaultRouter()
router.register(r'farmer', views.FarmerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'certificate', views.CertificateViewSet)
router.register(r'productfarmer', views.ProductFarmerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
