# Generated by Django 3.2.5 on 2021-11-13 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_customerinput_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinput',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customerinput',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customerinput',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='customerinput',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='bundle',
            field=models.CharField(choices=[('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('diamond', 'Diamond')], default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.CharField(blank=True, default='location', max_length=300),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='customer',
            name='phonenumber',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='types',
            field=models.CharField(choices=[('home', 'Home'), ('business', 'Business')], default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='app.user'),
            preserve_default=False,
        ),
    ]
