# Generated by Django 3.0.1 on 2021-11-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='productPrice',
            field=models.CharField(default=200, max_length=200),
            preserve_default=False,
        ),
    ]
