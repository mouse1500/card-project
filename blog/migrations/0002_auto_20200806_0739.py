# Generated by Django 3.0.7 on 2020-08-06 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bloc',
            new_name='Post',
        ),
    ]
