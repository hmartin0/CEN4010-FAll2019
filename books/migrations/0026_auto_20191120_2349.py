# Generated by Django 2.2.7 on 2019-11-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_auto_20191120_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]