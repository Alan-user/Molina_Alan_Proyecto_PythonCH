# Generated by Django 5.1.2 on 2024-11-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='años',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datosextra',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
