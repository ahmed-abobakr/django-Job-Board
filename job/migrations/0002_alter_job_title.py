# Generated by Django 3.2.6 on 2021-08-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
