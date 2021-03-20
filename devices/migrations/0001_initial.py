# Generated by Django 3.1.4 on 2021-02-15 14:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        ('customers', '0001_initial'),
        ('nets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('serialnumber', models.CharField(blank=True, max_length=50)),
                ('installation_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Device Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Device Manufacturers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WarrantyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Warranty Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateField()),
                ('valid_until', models.DateField()),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
                ('warranty_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.warrantytype')),
            ],
            options={
                'verbose_name_plural': 'Warranties',
                'ordering': ['customer'],
            },
        ),
        migrations.CreateModel(
            name='HardwareModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.devicemanufacturer')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceInNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('nic', models.CharField(blank=True, max_length=50, verbose_name='NIC')),
                ('mac_address', models.CharField(blank=True, max_length=50, verbose_name='MAC Address')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
                ('ip_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nets.ipstatus', verbose_name='IP Status')),
                ('net', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nets.net')),
            ],
            options={
                'verbose_name_plural': 'Devices in Net',
                'ordering': ['ip'],
            },
        ),
        migrations.AddField(
            model_name='device',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.devicecategory'),
        ),
        migrations.AddField(
            model_name='device',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.location'),
        ),
        migrations.AddField(
            model_name='device',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.devicemanufacturer'),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.hardwaremodel'),
        ),
        migrations.AddField(
            model_name='device',
            name='net',
            field=models.ManyToManyField(through='devices.DeviceInNet', to='nets.Net'),
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.owner'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]