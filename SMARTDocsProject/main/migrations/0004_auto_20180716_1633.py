# Generated by Django 2.0.4 on 2018-07-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180712_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttopractice',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='practice',
            name='type_of',
            field=models.SmallIntegerField(choices=[(0, 'Практика в лаборатории института'), (1, 'Практика на предприятии'), (2, 'Преддипломная практика')], default=0),
        ),
    ]
