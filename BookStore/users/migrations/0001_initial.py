# Generated by Django 2.2.5 on 2019-10-11 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, default='', max_length=30, verbose_name='Nick name')),
                ('bio', models.TextField(blank=True, max_length=450)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('expdate_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1)),
                ('expdate_year', models.IntegerField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029)], default=2019)),
                ('securitycode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=100, verbose_name='Address Lines 1')),
                ('address2', models.CharField(blank=True, max_length=100, verbose_name='Address Lines 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', localflavor.us.models.USStateField(default='FL', max_length=2, verbose_name='State')),
                ('zipcode', models.CharField(max_length=5, verbose_name='Zipcode')),
                ('slug', models.SlugField(max_length=150)),
                ('primaryAddress', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]