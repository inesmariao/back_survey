from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# CapituloI
class CapituloI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True)
    
    VIAJA_CON_CHOICES = [
        ('S', 'Solo'),
        ('A', 'Amigos'),
        ('T', 'Compañeros de trabajo'),
        ('F', 'Familia'),
        ('O', 'Otro'),
    ]
    viaja_con = models.CharField(max_length=1, choices=VIAJA_CON_CHOICES)
    viaja_con_otro = models.CharField(max_length=100, null=True, blank=True)  # Campo para especificar si se elige 'Otro'

    numero_personas = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.pais} - {self.nacionalidad}"

# CapituloII
class CapituloII(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    MOTIVO_VIAJE_CHOICES = [
        ('1', 'Visita a familiares o amigos'),
        ('2', 'Vacaciones (recreación, ocio, sol y playa)'),
        ('3', 'Compras'),
        ('4', 'Turismo Cultural'),
        ('5', 'Asistencia a eventos artísticos'),
        ('6', 'Estudio y/o formación'),
        ('7', 'Tratamiento de salud y belleza'),
        ('8', 'Religioso'),
        ('9', 'Asistencia a Congresos, Seminarios, convenciones'),
        ('10', 'Trabajo remunerado en destino'),
        ('11', 'Trabajo o negocios (no remunerado en destino)'),
        ('12', 'Participación en eventos artísticos y/o deportivos'),
        ('13', 'Tránsito'),
        ('14', 'Otro'),
    ]
    motivo_viaje = models.CharField(max_length=2, choices=MOTIVO_VIAJE_CHOICES)
    motivo_viaje_otro = models.CharField(max_length=100, null=True, blank=True)  # Campo para especificar si se elige 'Otro'

    ORGANIZACION_VIAJE_CHOICES = [
        ('1', 'Paquete turístico organizado por una agencia de viajes en Colombia'),
        ('2', 'Paquete turístico organizado por una agencia de viajes en el país de visita'),
        ('3', 'Paquete turístico organizado por terceros que no sean agencias de viajes'),
        ('4', 'Viaje organizado por cuenta propia'),
        ('5', 'Otro'),
    ]
    organizacion_viaje = models.ManyToManyField('OrganizacionViaje')
    organizacion_viaje_otro = models.CharField(max_length=100, null=True, blank=True)  # Campo para especificar si se elige 'Otro'

    SERVICIOS_PAQUETE_CHOICES = [
        ('1', 'Alojamiento'),
        ('2', 'Transporte internacional'),
        ('3', 'Alimentos y bebidas (No incluidos en el alojamiento)'),
        ('4', 'Servicios culturales y de entretenimiento'),
        ('5', 'Servicios deportivos y recreacionales (Ej.: Actividades de aventura, ecológicas, otros)'),
        ('6', 'Tours en destino (con servicio de guía)'),
        ('7', 'Transporte aéreo interno en el destino'),
    ]
    servicios_paquete = models.ManyToManyField('ServiciosPaquete')
    transporte_interno_otro = models.CharField(max_length=100, null=True, blank=True)  # Campo para especificar otro transporte interno
    otro_servicio = models.CharField(max_length=100, null=True, blank=True)  # Campo para especificar otro servicio

class OrganizacionViaje(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class ServiciosPaquete(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

# CapituloIII
class Moneda(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_divisa = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_divisa})"

class CapituloIII(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    gasto_paquete_turistico = models.BooleanField()
    valor_paquete_usted = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_paquete_usted = models.ForeignKey(Moneda, related_name='moneda_paquete_usted', on_delete=models.CASCADE)
    valor_paquete_terceros_no_grupo = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_paquete_terceros_no_grupo = models.ForeignKey(Moneda, related_name='moneda_paquete_terceros_no_grupo', on_delete=models.CASCADE)
    valor_paquete_terceros_si_grupo = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_paquete_terceros_si_grupo = models.ForeignKey(Moneda, related_name='moneda_paquete_terceros_si_grupo', on_delete=models.CASCADE)
    personas_paquete = models.IntegerField()

    gasto_transporte_internacional = models.BooleanField()
    valor_transporte_usted = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_transporte_usted = models.ForeignKey(Moneda, related_name='moneda_transporte_usted', on_delete=models.CASCADE)
    valor_transporte_terceros_no_grupo = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_transporte_terceros_no_grupo = models.ForeignKey(Moneda, related_name='moneda_transporte_terceros_no_grupo', on_delete=models.CASCADE)
    valor_transporte_terceros_si_grupo = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_transporte_terceros_si_grupo = models.ForeignKey(Moneda, related_name='moneda_transporte_terceros_si_grupo', on_delete=models.CASCADE)
    personas_transporte = models.IntegerField()

    # Esta relación permite múltiples países visitados
    paises_visitados = models.ManyToManyField(Pais, through='PaisVisita')

    def __str__(self):
        return f"{self.user.username} - {self.id}"

class PaisVisita(models.Model):
    capitulo = models.ForeignKey(CapituloIII, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    noches_vivienda_propia = models.IntegerField()
    noches_hotel = models.IntegerField()
    noches_vivienda_familiar_amigos = models.IntegerField()
    noches_vivienda_alquiler = models.IntegerField()
    noches_otro_tipo_vivienda = models.IntegerField()

    def __str__(self):
        return f"{self.capitulo} - {self.pais}"