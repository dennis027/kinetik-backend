# Generated by Django 3.2.5 on 2021-11-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211105_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admininput',
            name='recomendations',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='admininput',
            name='remarks',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='admininput',
            name='status',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
