# Generated by Django 3.2.5 on 2022-04-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0013_user_year"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="year",),
        migrations.AddField(
            model_name="photo", name="year", field=models.IntegerField(default=2022),
        ),
    ]
