# Generated by Django 5.1.7 on 2025-03-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseMaterials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasematerial',
            name='type',
            field=models.CharField(default='', max_length=255, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='purchasematerial',
            name='material',
            field=models.CharField(default='', max_length=255, verbose_name='Material'),
        ),
    ]
