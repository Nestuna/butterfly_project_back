# Generated by Django 3.1.4 on 2021-01-12 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='nb_user',
            new_name='nb_users',
        ),
    ]
