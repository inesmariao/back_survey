# Generated by Django 5.0.7 on 2024-07-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gasto_paquete_turistico', models.BooleanField()),
                ('valor_paquete_usted', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda_paquete_usted', models.CharField(max_length=10)),
                ('valor_paquete_terceros_no_grupo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda_paquete_terceros_no_grupo', models.CharField(max_length=10)),
                ('valor_paquete_terceros_si_grupo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda_paquete_terceros_si_grupo', models.CharField(max_length=10)),
                ('personas_paquete', models.IntegerField()),
                ('gasto_transporte_internacional', models.BooleanField()),
                ('valor_transporte_usted', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda_transporte_usted', models.CharField(max_length=10)),
                ('valor_transporte_terceros_no_grupo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda_transporte_terceros_no_grupo', models.CharField(max_length=10)),
                ('valor_transporte_terceros_si_grupo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda_transporte_terceros_si_grupo', models.CharField(max_length=10)),
                ('personas_transporte', models.IntegerField()),
                ('pais_visita', models.CharField(max_length=100)),
                ('noches_vivienda_propia', models.IntegerField()),
                ('noches_hotel', models.IntegerField()),
                ('noches_vivienda_familiar_amigos', models.IntegerField()),
                ('noches_vivienda_alquiler', models.IntegerField()),
                ('noches_otro_tipo_vivienda', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TripDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposito_viaje', models.CharField(max_length=255)),
                ('tipo_acompanante', models.CharField(max_length=100)),
                ('medio_transporte', models.CharField(max_length=100)),
                ('frecuencia_viaje', models.CharField(max_length=100)),
                ('duracion_estadia', models.CharField(max_length=100)),
                ('fecha_inicio_viaje', models.DateField()),
                ('fecha_fin_viaje', models.DateField()),
            ],
        ),
    ]