# Generated by Django 4.2.7 on 2024-03-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes_predictor', '0003_diabetesinput_age_diabetesinput_diabetespedigree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diabetesinput',
            name='Prediction',
            field=models.IntegerField(default=0),
        ),
    ]