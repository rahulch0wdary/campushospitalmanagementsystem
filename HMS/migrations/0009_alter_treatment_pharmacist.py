# Generated by Django 3.2.4 on 2021-06-04 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0008_auto_20210604_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='pharmacist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMS.pharmcistdetails'),
        ),
    ]