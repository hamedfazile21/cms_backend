# Generated by Django 5.1.7 on 2025-03-24 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customerStatus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentFactor',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('related_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='customerStatus.createcustomer')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentPlane',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('related_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='customerStatus.createcustomer')),
            ],
        ),
        migrations.CreateModel(
            name='FactorItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teeth_number', models.CharField(max_length=255)),
                ('teeth_problem', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('remainder', models.IntegerField()),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factor', to='customerFactor.treatmentfactor')),
            ],
        ),
        migrations.CreateModel(
            name='PlaneItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teeth_number', models.CharField(max_length=255)),
                ('teeth_problem', models.CharField(max_length=255)),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='customerFactor.treatmentplane')),
            ],
        ),
    ]
