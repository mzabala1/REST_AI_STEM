# Generated by Django 2.0.4 on 2018-05-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STEM', '0005_remove_predecidos_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Predecidos',
        ),
    ]