# Generated by Django 2.1 on 2019-03-08 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_word', models.CharField(max_length=200)),
                ('meaning', models.TextField()),
                ('make_sentence', models.TextField()),
                ('word_added', models.DateTimeField(default=datetime.datetime(2019, 3, 8, 18, 16, 17, 141989))),
            ],
        ),
    ]