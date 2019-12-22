from api_rest.models import Farmer, Product, Certificate, ProductFarmer
from rest_framework import viewsets
from api_rest.serializers import FarmerSerializer, ProductSerializer, CertificateSerializer, ProductFarmerSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farmers to be viewed or edited.
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows certificate to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ProductFarmerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ProductFarmer to be viewed or edited.
    """
    queryset = ProductFarmer.objects.all()
    serializer_class = ProductFarmerSerializer