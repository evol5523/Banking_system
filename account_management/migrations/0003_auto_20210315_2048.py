# Generated by Django 3.1.7 on 2021-03-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0002_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('checking', 'checking'), ('savings', 'savings'), ('credit', 'credit')], max_length=10),
        ),
    ]
