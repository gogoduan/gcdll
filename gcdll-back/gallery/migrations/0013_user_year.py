# Generated by Django 3.2.5 on 2022-04-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0012_gallery_layout"),
    ]

    operations = [
        migrations.AddField(
            model_name="user", name="year", field=models.IntegerField(default=2022),
        ),
    ]
