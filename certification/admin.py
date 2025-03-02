from django.contrib import admin
from .models import *

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(SubSede)
class SubSedeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion')
    search_fields = ('nombre', 'direccion')

@admin.register(Subdirectores)
class SubdirectoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cargo', 'regional', 'sede', 'created_at')
    search_fields = ('nombre', 'apellido', 'regional', 'sede')
    list_filter = ('cargo', 'regional', 'sede')

@admin.register(UsuarioInstructor)
class UsuarioInstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'estado_usuario', 'cargo', 'sede', 'created_at')
    search_fields = ('nombre', 'apellido', 'estado_usuario')
    list_filter = ('estado_usuario', 'cargo', 'sede')

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('id_instructor', 'fecha_nacimiento', 'sexo', 'pais_residencia', 'cel')
    search_fields = ('id_instructor__nombre', 'id_instructor__apellido', 'pais_residencia')
    list_filter = ('sexo', 'pais_residencia')

@admin.register(HistorialCertificados)
class HistorialCertificadosAdmin(admin.ModelAdmin):
    list_display = ('usuario_instructor', 'n_contrato', 'created_at')
    search_fields = ('usuario_instructor__nombre', 'usuario_instructor__apellido', 'n_contrato')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'n_contrato', 'id_instructor', 'id_cargo', 'fecha_inicio', 'fecha_fin', 'valor_contrato')
    search_fields = ('n_contrato', 'id_instructor__nombre', 'id_instructor__apellido')
    list_filter = ('fecha_inicio', 'fecha_fin', 'id_cargo')

@admin.register(EstadoContrato)
class EstadoContratoAdmin(admin.ModelAdmin):
    list_display = ('n_contrato', 'estado')
    search_fields = ('n_contrato__n_contrato',)
    list_filter = ('estado',)

@admin.register(Proroga)
class ProrogaAdmin(admin.ModelAdmin):
    list_display = ('n_contrato', 'vigencia_prorroga', 'adicion')
    search_fields = ('n_contrato__n_contrato',)

@admin.register(Obligaciones)
class ObligacionesAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'obligaciones_especificas')
    search_fields = ('contrato__n_contrato',)
