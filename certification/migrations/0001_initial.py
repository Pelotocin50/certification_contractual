# Generated by Django 5.1.6 on 2025-02-21 21:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('estado_usuario', models.CharField(blank=True, choices=[('disabled', 'INHABILITADO'), ('active', 'ACTIVO')], max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.cargo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_instructor_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SubSede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_contrato', models.CharField(max_length=255)),
                ('date_contrat', models.DateField()),
                ('object_contrato', models.TextField()),
                ('plazo_ejecucion', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('valor_contrato', models.DecimalField(decimal_places=2, max_digits=15)),
                ('valor_honorario', models.DecimalField(decimal_places=2, max_digits=15)),
                ('forma_pago', models.CharField(max_length=255)),
                ('prorroga', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.cargo')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='contrato_updated', to=settings.AUTH_USER_MODEL)),
                ('id_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.usuarioinstructor')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoContrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('disabled', 'INHABILITADO'), ('active', 'ACTIVO')], max_length=15, null=True)),
                ('n_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.contrato')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCertificados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_contrato', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('usuario_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.usuarioinstructor')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Obligaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obligaciones_especificas', models.TextField()),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Proroga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vigencia_prorroga', models.CharField(max_length=255)),
                ('adicion', models.DecimalField(decimal_places=2, max_digits=15)),
                ('n_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Subdirectores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('regional', models.CharField(max_length=255)),
                ('sede', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='certification.cargo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='id_subdirector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.subdirectores'),
        ),
        migrations.AddField(
            model_name='usuarioinstructor',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.subsede'),
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id_instructor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='certification.usuarioinstructor')),
                ('fecha_nacimiento', models.DateField()),
                ('pais_nacimiento', models.CharField(max_length=100)),
                ('departamento_nacimiento', models.CharField(max_length=100)),
                ('municipio_nacimiento', models.CharField(max_length=100)),
                ('fecha_expedicion', models.DateField()),
                ('lugar_expedicion', models.CharField(max_length=255)),
                ('tipo_sangre', models.CharField(max_length=10)),
                ('sexo', models.CharField(blank=True, choices=[('male', 'MASCULINO'), ('female', 'FEMENINO')], max_length=10, null=True)),
                ('eps', models.CharField(max_length=255)),
                ('pais_residencia', models.CharField(max_length=100)),
                ('dpt_residencia', models.CharField(max_length=100)),
                ('mun_residencia', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('c_personal', models.CharField(max_length=255)),
                ('c_empresarial', models.CharField(blank=True, max_length=255, null=True)),
                ('tel1', models.CharField(blank=True, max_length=20, null=True)),
                ('tel2', models.CharField(blank=True, max_length=20, null=True)),
                ('cel', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
