# Generated by Django 2.2 on 2019-06-27 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0004_auto_20190627_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('CAD', 'CAD')], default='USD', max_length=3),
        ),
    ]
