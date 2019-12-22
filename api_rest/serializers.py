from rest_framework import serializers
from api_rest.models import Farmer, Product, Certificate, ProductFarmer


class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = ['farmer_name', 'street', 'cp', 'city', 'siret']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'international_codification', 'unit', 'farmer']


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certificate_name', 'certificate_type', 'farmer']


class ProductFarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductFarmer
        fields = ['special_name', 'product', 'farmer']
