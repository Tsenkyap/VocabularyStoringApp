# Generated by Django 2.1 on 2019-06-10 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordmeaning', '0004_auto_20190610_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 10, 10, 42, 54, 611793)),
        ),
    ]