# Generated by Django 3.1.1 on 2020-11-12 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kito', '0008_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kito',
            old_name='image',
            new_name='img',
        ),
    ]
