# Generated by Django 2.2.7 on 2019-11-16 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.Profile'),
            preserve_default=False,
        ),
    ]