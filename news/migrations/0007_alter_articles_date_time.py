# Generated by Django 4.0.1 on 2022-02-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date_time',
            field=models.DateTimeField(verbose_name='Время создания'),
        ),
    ]
