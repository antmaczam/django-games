# Generated by Django 2.2.7 on 2020-01-20 22:37

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200120_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rate',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
