# Generated by Django 2.0.4 on 2018-05-29 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('STEM', '0009_preguntas'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='respuestac',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='respuestaf1',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='respuestaf2',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='respuestaf3',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
