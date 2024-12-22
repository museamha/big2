# Generated by Django 5.1.4 on 2024-12-22 11:35

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Middle_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('location', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('details', models.TextField()),
                ('terms1', models.BooleanField()),
                ('terms2', models.BooleanField()),
                ('terms3', models.BooleanField()),
                ('Service_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service_type')),
            ],
        ),
    ]