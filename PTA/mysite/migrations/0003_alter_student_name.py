# Generated by Django 4.1.3 on 2022-11-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_subject_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]
