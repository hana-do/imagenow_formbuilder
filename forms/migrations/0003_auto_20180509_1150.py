# Generated by Django 2.0.5 on 2018-05-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20180509_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='form',
            new_name='file_path',
        ),
        migrations.AddField(
            model_name='form',
            name='form_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='form_notes',
            field=models.TextField(null=True),
        ),
    ]