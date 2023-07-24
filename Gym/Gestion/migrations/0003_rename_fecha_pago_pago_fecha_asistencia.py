# Generated by Django 4.1.5 on 2023-01-09 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_pago'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pago',
            old_name='fecha_pago',
            new_name='fecha',
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('dni_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.cliente')),
            ],
        ),
    ]
