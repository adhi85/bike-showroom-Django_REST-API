# Generated by Django 4.1.3 on 2022-11-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='modelNumber',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]