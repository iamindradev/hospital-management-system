# Generated by Django 2.0 on 2020-06-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200613_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mobile_number',
            field=models.CharField(max_length=50),
        ),
    ]
