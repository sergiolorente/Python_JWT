# Generated by Django 2.0.6 on 2018-07-10 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Descripción')),
                ('lat', models.DecimalField(decimal_places=6, default=0, max_digits=20, verbose_name='Latitud')),
                ('lon', models.DecimalField(decimal_places=6, default=0, max_digits=20, verbose_name='Longitud')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('user', models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['-title'],
            },
        ),
    ]
