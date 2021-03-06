# Generated by Django 4.0.1 on 2022-01-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_userdata_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='currency',
            field=models.CharField(choices=[('USD', 'Dollars'), ('EUR', 'Euros'), ('GBP', 'Pounds')], max_length=3),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
