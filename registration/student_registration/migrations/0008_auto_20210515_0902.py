# Generated by Django 3.1.7 on 2021-05-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0007_auto_20210515_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='enrolment_for_year',
            field=models.IntegerField(null=True),
        ),
    ]