# Generated by Django 4.0.4 on 2022-04-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='isActive',
            field=models.BooleanField(blank=True, null=True, verbose_name='still active?'),
        ),
    ]