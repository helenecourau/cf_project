from django.db import models

class Certificate(models.Model):
    
    biologique = 'bio'
    ogm = 'ogm'
    origine = 'or'
    
    certificate_type_choices = [
        (biologique, 'Biologique'),
        (ogm, 'Sans OGM'),
        (origine, 'Origine'),
    ]

    certificate_name = models.CharField(
        max_length=255,
        verbose_name="Nom du certificat", 
        unique=True)

    certificate_type = models.CharField(
    	max_length=255,
        choices=certificate_type_choices,
        default=biologique,
        verbose_name="type",
    )

    farmer = models.ForeignKey('Farmer', on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "Certificat"

    def __str__(self):

        return self.certificate_name

class Farmer(models.Model):

    farmer_name = models.CharField(
        max_length=255,
        verbose_name="Raison sociale", 
        unique=True)

    street = models.CharField(
        max_length=255,
        verbose_name="Rue", 
        null=True)

    cp = models.IntegerField(
        verbose_name="Code postal", 
        null=True)

    city = models.CharField(
        max_length=255,
        verbose_name="Ville", 
        null=True)

    siret = models.BigIntegerField(
        verbose_name="SIRET", 
        null=True)

    class Meta:
        verbose_name = "Exploitation agricole"

    def __str__(self):

        return self.farmer_name

class Product(models.Model):

    product_name = models.CharField(
        max_length=255,
        verbose_name="Nom du produit", 
        unique=True)

    international_codification = models.CharField(
        max_length=255,
        verbose_name="Codification internationale", 
        null=True)

    unit = models.CharField(
        max_length=255,
        verbose_name="Unité", 
        null=True)

    farmer = models.ManyToManyField(
        Farmer,
        through='ProductFarmer',
    )


    class Meta:
        verbose_name = "Produit"

    def __str__(self):

        return self.product_name


class ProductFarmer(models.Model):
    special_name = models.CharField(
        max_length=255,
        verbose_name="Nom spécifique", 
        null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.product, self.farmer)
