# Generated by Django 4.1 on 2022-11-12 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chuch', '0013_joinus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joinus',
            old_name='User_email',
            new_name='user_email',
        ),
    ]
