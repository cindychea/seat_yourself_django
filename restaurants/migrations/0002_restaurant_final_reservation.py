# Generated by Django 2.1.5 on 2019-06-04 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='final_reservation',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
