# Generated by Django 2.0.5 on 2018-05-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20180509_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='form_instruction',
            field=models.TextField(null=True),
        ),
    ]
