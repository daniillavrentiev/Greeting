# Generated by Django 4.0.1 on 2022-01-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_greeting_last_name_alter_greeting_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name="Ім'я"),
        ),
    ]