# Generated by Django 3.0.8 on 2020-08-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionslist',
            name='price',
            field=models.CharField(max_length=3000),
        ),
    ]
