# Generated by Django 5.2 on 2025-04-30 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('min_size', models.PositiveIntegerField(default=36, verbose_name='Минимальный размер')),
                ('max_size', models.PositiveIntegerField(default=52, verbose_name='Максимальный размер')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')),
                ('is_exists', models.BooleanField(default=True, verbose_name='В наличии?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
                ('collection', models.ManyToManyField(to='shop.collection', verbose_name='Коллекция')),
            ],
            options={
                'verbose_name': 'Одежда',
                'verbose_name_plural': 'Одежды',
            },
        ),
    ]
