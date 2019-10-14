# Generated by Django 2.2.6 on 2019-10-14 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_books_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bookRating',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='books',
            name='publisherDate',
            field=models.CharField(default='no date', max_length=20),
        ),
        migrations.AddField(
            model_name='books',
            name='publisherName',
            field=models.CharField(default='no name', max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books')),
            ],
        ),
    ]
