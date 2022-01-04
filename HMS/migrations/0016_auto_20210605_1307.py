# Generated by Django 3.2.4 on 2021-06-05 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0015_auto_20210605_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultymedicine',
            name='treatment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HMS.facultytreatment'),
        ),
        migrations.AddField(
            model_name='studentmedicine',
            name='treatment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HMS.studenttreatment'),
        ),
    ]