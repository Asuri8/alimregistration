# Generated by Django 2.2.7 on 2021-07-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0029_auto_20210718_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='current_islamic_grade',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
