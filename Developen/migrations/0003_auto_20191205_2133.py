# Generated by Django 2.1.7 on 2019-12-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developen', '0002_auto_20191205_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reward',
            field=models.CharField(default='default reward', max_length=100),
        ),
    ]
