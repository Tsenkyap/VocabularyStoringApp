# Generated by Django 2.1 on 2019-06-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordmeaning', '0005_auto_20190610_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
