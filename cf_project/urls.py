from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api_rest import views

router = routers.DefaultRouter()
router.register(r'farmer',
                views.FarmerViewSet,
                basename='farmer')
router.register(r'product',
                views.ProductViewSet)
router.register(r'certificate',
                views.CertificateViewSet,
                basename='certificate')
router.register(r'productfarmer',
                views.ProductFarmerViewSet)
router.register(r'certificateproductfarmer',
                views.FarmerProductCertificateViewSet,
                basename='certificateproductfarmer')
router.register(r'filtercertificate',
                views.FilterCertificateViewSet,
                basename='filtercertificate')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='home'),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
