# Generated by Django 4.0.1 on 2022-01-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('bio', models.TextField(max_length=280)),
                ('website_link_1', models.URLField()),
                ('website_link_2', models.URLField()),
                ('website_link_3', models.URLField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('currency', models.CharField(choices=[('USD', 'Dollars'), ('EUR', 'Euros'), ('GBP', 'Pounds')], max_length=3)),
            ],
        ),
    ]