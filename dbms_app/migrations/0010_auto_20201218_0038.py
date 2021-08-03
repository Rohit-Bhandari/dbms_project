# Generated by Django 3.1.3 on 2020-12-17 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbms_app', '0009_auto_20201217_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='agentid',
            field=models.ForeignKey(blank=True, db_column='AgentId', null=True, on_delete=django.db.models.deletion.CASCADE, to='dbms_app.agent'),
        ),
        migrations.AlterModelTable(
            name='agent',
            table='agent',
        ),
    ]
