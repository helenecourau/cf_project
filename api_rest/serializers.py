from rest_framework import serializers
from api_rest.models import Farmer, Product, Certificate, ProductFarmer


class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id','farmer_name', 'street', 'cp', 'city', 'siret']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'international_codification',
                  'unit', 'farmer']


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'certificate_name', 'certificate_type', 'farmer']


class ProductFarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductFarmer
        fields = ['id', 'special_name', 'product', 'farmer']


class FarmerProductCertificateSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    certificates = serializers.StringRelatedField(many=True)

    class Meta:
        model = Farmer
        fields = ['id', 'farmer_name', 'products', 'certificates']
