# Generated by Django 4.2.16 on 2024-11-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20200508_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]