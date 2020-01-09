from django.contrib.auth.forms import SetPasswordForm
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


class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128, label="New password")
    new_password2 = serializers.CharField(max_length=128, label="Enter new password again")

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(
            settings, 'OLD_PASSWORD_FIELD_ENABLED', False
        )
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise serializers.ValidationError('Invalid password')
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(self.request, self.user)
