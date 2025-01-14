# Generated by Django 4.2.7 on 2024-02-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glucose', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('pregancies', models.IntegerField()),
                ('Skin_Thickness', models.IntegerField()),
                ('BMI', models.FloatField()),
                ('Insulin', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Diabetes_Pedigree', models.FloatField()),
            ],
        ),
    ]
