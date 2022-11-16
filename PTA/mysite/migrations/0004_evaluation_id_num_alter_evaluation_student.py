# Generated by Django 4.1.3 on 2022-11-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='id_num',
            field=models.IntegerField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='mysite.student'),
        ),
    ]