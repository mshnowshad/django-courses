# Generated by Django 5.0 on 2024-01-30 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='id',
            new_name='msg_id',
        ),
    ]