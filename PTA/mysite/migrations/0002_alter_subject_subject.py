# Generated by Django 4.1.3 on 2022-11-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
