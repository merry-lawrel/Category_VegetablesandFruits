# Generated by Django 4.1.5 on 2023-02-23 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_15', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catsample',
            old_name='image',
            new_name='catimage',
        ),
        migrations.RenameField(
            model_name='catsample',
            old_name='name',
            new_name='catname',
        ),
    ]
