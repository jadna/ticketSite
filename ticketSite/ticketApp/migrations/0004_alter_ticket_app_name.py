# Generated by Django 4.1.5 on 2023-01-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0003_ticket_app_name_alter_ticket_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='app_name',
            field=models.CharField(choices=[('Aplication 1', 'App1'), ('Aplication 2', 'App2'), ('Aplication 3', 'App3'), ('Aplication 4', 'App4')], max_length=30),
        ),
    ]
