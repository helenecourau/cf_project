# Generated by Django 2.2.4 on 2019-12-23 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0008_auto_20191223_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='api_rest.Farmer'),
        ),
    ]
