# Generated by Django 2.0 on 2020-06-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_appointment_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationp',
            name='status',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(db_column='patient_id', null=True, on_delete='DO_NOTHING', to='patient.registrationp'),
        ),
    ]