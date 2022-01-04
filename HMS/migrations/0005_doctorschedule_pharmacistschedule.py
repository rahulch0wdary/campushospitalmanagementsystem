# Generated by Django 3.1 on 2021-06-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0004_pharmcistdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(max_length=10, unique=True)),
                ('slot1', models.CharField(max_length=20, null=True)),
                ('slot2', models.CharField(max_length=20, null=True)),
                ('slot3', models.CharField(max_length=20, null=True)),
                ('slot4', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PharmacistSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(max_length=10, unique=True)),
                ('slot1', models.CharField(max_length=20, null=True)),
                ('slot2', models.CharField(max_length=20, null=True)),
                ('slot3', models.CharField(max_length=20, null=True)),
                ('slot4', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]