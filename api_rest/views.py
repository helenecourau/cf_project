from api_rest.models import Farmer, Product, Certificate, ProductFarmer
from rest_framework import viewsets, permissions
from api_rest.serializers import FarmerSerializer, ProductSerializer,\
                                 CertificateSerializer,\
                                 ProductFarmerSerializer,\
                                 FarmerProductCertificateSerializer


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


class FarmerProductCertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to filter farmers
    and their products and certificates.
    """
    serializer_class = FarmerProductCertificateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):

        queryset = Farmer.objects.all()
        farmer = self.request.query_params.get('farmer_name', None)
        if farmer is not None:
            queryset = queryset.filter(farmer_name=farmer)
        return queryset


class FilterCertificateViewSet(CertificateViewSet):
    """
    API endpoint that allows user to filter certificates.
    """

    def get_queryset(self):
        queryset = Certificate.objects.all()
        certificate = self.request.query_params.get('certificate_type', None)
        if certificate is not None:
            queryset = queryset.filter(certificate_type=certificate)
        return queryset
