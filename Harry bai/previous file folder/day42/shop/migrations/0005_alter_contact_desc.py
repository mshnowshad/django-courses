# Generated by Django 5.0 on 2024-01-27 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_contact_msg_id_contact_id_alter_contact_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
