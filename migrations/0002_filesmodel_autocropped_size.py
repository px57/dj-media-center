# Generated by Django 4.2 on 2023-09-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesmodel',
            name='autocropped_size',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]