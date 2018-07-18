# Generated by Django 2.0.4 on 2018-07-11 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentToPractice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='practice',
            name='curator',
            field=models.ForeignKey(limit_choices_to=main.models.get_only_curators_q, on_delete=django.db.models.deletion.CASCADE, related_name='curator_practices', to=settings.AUTH_USER_MODEL, verbose_name='Куратор'),
        ),
        migrations.AddField(
            model_name='studenttopractice',
            name='practice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practice_relations', to='main.Practice', verbose_name='Практика'),
        ),
        migrations.AddField(
            model_name='studenttopractice',
            name='student',
            field=models.ForeignKey(limit_choices_to=main.models.get_only_students_q, on_delete=django.db.models.deletion.CASCADE, related_name='student_relations', to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='practice',
            name='students',
            field=models.ManyToManyField(related_name='student_practices', through='main.StudentToPractice', to=settings.AUTH_USER_MODEL),
        ),
    ]
