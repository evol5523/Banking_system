# Generated by Django 3.1.7 on 2021-03-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0003_auto_20210315_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('savings', 'savings'), ('checking', 'checking'), ('credit', 'credit')], max_length=10),
        ),
    ]
