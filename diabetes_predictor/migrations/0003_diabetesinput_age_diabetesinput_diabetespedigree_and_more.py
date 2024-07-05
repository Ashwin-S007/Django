# Generated by Django 4.2.7 on 2024-03-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes_predictor', '0002_rename_bmi_diabetesinput_bmi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diabetesinput',
            name='Age',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='diabetesinput',
            name='DiabetesPedigree',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='diabetesinput',
            name='insulin',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='diabetesinput',
            name='pregnancies',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='diabetesinput',
            name='skinthickness',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='diabetesinput',
            name='blood_pressure',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='diabetesinput',
            name='bmi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='diabetesinput',
            name='glucose',
            field=models.FloatField(default=0),
        ),
    ]