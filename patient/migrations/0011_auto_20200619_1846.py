# Generated by Django 2.0 on 2020-06-19 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_auto_20200619_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doct_key',
            new_name='doct',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient',
            new_name='pt',
        ),
    ]
