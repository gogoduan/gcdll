# Generated by Django 4.0.3 on 2022-05-09 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0022_gallery_user_alter_gallery_like_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="gallery.user"
            ),
        ),
    ]
