# Generated by Django 3.1.13 on 2021-10-18 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'IP Status',
                'verbose_name_plural': 'IP Status',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_range', models.CharField(max_length=50, verbose_name='IP Range')),
                ('dhcp_range', models.CharField(max_length=50, verbose_name='DHCP Range')),
                ('description', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
