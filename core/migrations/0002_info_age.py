# Generated by Django 4.1.7 on 2023-02-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]