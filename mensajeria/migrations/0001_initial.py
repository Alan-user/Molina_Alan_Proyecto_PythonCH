# Generated by Django 5.1.2 on 2024-11-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinatario', models.CharField(max_length=30)),
                ('remitente', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('cuerpo', models.CharField(max_length=500)),
                ('asunto', models.CharField(max_length=100)),
            ],
        ),
    ]
