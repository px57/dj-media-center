# Generated by Django 4.2 on 2023-09-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacenter', '0002_filesmodel_autocropped_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesmodel',
            name='mime_type',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]