# Generated by Django 4.1.13 on 2024-02-19 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
