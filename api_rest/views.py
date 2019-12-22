from api_rest.models import Farmer, Product, Certificate, ProductFarmer
from rest_framework import viewsets, permissions
from api_rest.serializers import FarmerSerializer, ProductSerializer, CertificateSerializer, ProductFarmerSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farmers to be viewed or edited.
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows certificates to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductFarmerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ProductFarmer relations to be viewed or edited.
    """
    queryset = ProductFarmer.objects.all()
    serializer_class = ProductFarmerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]