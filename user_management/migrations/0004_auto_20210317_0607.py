# Generated by Django 3.1.7 on 2021-03-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_auto_20210315_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externaluser',
            name='user_type',
            field=models.CharField(choices=[('customer', 'customer'), ('t1', 't1'), ('t2', 't2'), ('t3', 't3')], max_length=10),
        ),
    ]
