# Generated by Django 5.0.4 on 2024-04-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('cover_image_url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]