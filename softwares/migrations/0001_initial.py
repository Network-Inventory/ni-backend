# Generated by Django 3.1.4 on 2021-02-15 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareArchitecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Software Architectures',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SoftwareCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Software Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='softwares.softwarecategory')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('architecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='softwares.softwarearchitecture')),
            ],
            options={
                'verbose_name_plural': 'Operating Systems',
                'ordering': ['name'],
            },
        ),
    ]