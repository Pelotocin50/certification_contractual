from django.db import models
from django.contrib.auth.models import User # modelo User de Django


class Cargo(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    
class SubSede(models.Model):
    direccion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Subdirectores(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)
    regional = models.CharField(max_length=255)
    sede = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Agrega la fecha de creación

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class UsuarioInstructor(models.Model):
    STATUS = [
        ('disabled', 'INHABILITADO'),
        ('active', 'ACTIVO'),
    ]
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    estado_usuario = models.CharField(max_length=15, choices=STATUS, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE) # relación de uno a muchos entre dos modelos
    sede = models.ForeignKey(SubSede, on_delete=models.CASCADE) # relación de uno a muchos entre dos modelos

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Agrega la fecha de creación
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='usuario_instructor_updated')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class DatosPersonales(models.Model):
    TYPE_SEX = [
        ('male', 'MASCULINO'),
        ('female', 'FEMENINO'),
    ]
    id_instructor = models.OneToOneField(UsuarioInstructor, on_delete=models.CASCADE, primary_key=True)
    fecha_nacimiento = models.DateField() # fecha de naciemiento
    pais_nacimiento = models.CharField(max_length=100) # pais de naciemiento
    departamento_nacimiento = models.CharField(max_length=100) # departamento de naciemiento
    municipio_nacimiento = models.CharField(max_length=100) # municipio de naciemiento
    fecha_expedicion = models.DateField() # fecha de expedición
    lugar_expedicion = models.CharField(max_length=255) # lugar de expedicion
    tipo_sangre = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10, choices=TYPE_SEX, null=True, blank=True)
    eps = models.CharField(max_length=255)
    pais_residencia = models.CharField(max_length=100) # pais_residente
    dpt_residencia = models.CharField(max_length=100) # dpt_residente
    mun_residencia = models.CharField(max_length=100) # mun_residente
    direccion = models.CharField(max_length=255)
    c_personal = models.CharField(max_length=255)
    c_empresarial = models.CharField(max_length=255, null=True, blank=True)
    tel1 = models.CharField(max_length=20, null=True, blank=True)
    tel2 = models.CharField(max_length=20, null=True, blank=True)
    cel = models.CharField(max_length=20)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Agrega la fecha de creación

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id_instructor)

class HistorialCertificados(models.Model):
    usuario_instructor = models.ForeignKey(UsuarioInstructor, on_delete=models.CASCADE)
    n_contrato = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Agrega la fecha de creación

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Certificado de {self.usuario_instructor}"
    
class Contrato(models.Model):
    id_instructor = models.ForeignKey(UsuarioInstructor, on_delete=models.CASCADE)
    n_contrato = models.CharField(max_length=255)
    date_contrat = models.DateField()
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    id_subdirector = models.ForeignKey(Subdirectores, on_delete=models.CASCADE)
    object_contrato = models.TextField()
    plazo_ejecucion = models.CharField(max_length=255) # plazo ejecucion
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor_contrato = models.DecimalField(max_digits=15, decimal_places=2)
    valor_honorario = models.DecimalField(max_digits=15, decimal_places=2)
    forma_pago = models.CharField(max_length=255) # forma de pago
    prorroga = models.BooleanField(default=False) # Prorroga

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Agrega la fecha de creación

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.RESTRICT, related_name='contrato_updated')

    def __str__(self):
        return f"Contrato {self.n_contrato} - {self.id_instructor}"

class EstadoContrato(models.Model):
    STATUS = [
        ('disabled', 'INHABILITADO'),
        ('active', 'ACTIVO'),
    ]
    n_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15, choices=STATUS, null=True, blank=True)

    def __str__(self):
        return f"Estado {self.estado} - {self.n_contrato}"

class Proroga(models.Model):
    n_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    vigencia_prorroga = models.CharField(max_length=255)
    adicion = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Prórroga del contrato {self.n_contrato}"

class Obligaciones(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    obligaciones_especificas = models.TextField()

    def __str__(self):
        return f"Obligaciones del contrato {self.contrato}"