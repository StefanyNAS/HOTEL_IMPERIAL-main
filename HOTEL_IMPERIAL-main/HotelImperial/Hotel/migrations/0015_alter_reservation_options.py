# Generated by Django 4.0.5 on 2022-08-11 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0014_reservation_client_reservation_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['client'], 'verbose_name': 'Reservacion', 'verbose_name_plural': 'Reservaciones'},
        ),
    ]