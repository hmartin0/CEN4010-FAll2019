# Generated by Django 2.2.7 on 2019-11-20 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=15)),
                ('authorBio', models.TextField(default='default')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=200)),
                ('bookSummary', models.TextField(default='hello')),
                ('bookRating', models.CharField(default='1', max_length=1)),
                ('bookPrice', models.DecimalField(decimal_places=2, default=2.22, max_digits=10)),
                ('genre', models.CharField(max_length=20)),
                ('cover', models.ImageField(default='default.jpg', upload_to='bookCovers')),
                ('publisherName', models.CharField(default='no name', max_length=20)),
                ('publisherDate', models.CharField(default='no date', max_length=20)),
                ('authorName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Author')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]