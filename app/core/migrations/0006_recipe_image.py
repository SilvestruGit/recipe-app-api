# Generated by Django 3.2.13 on 2022-06-17 13:43

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_ingredient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]