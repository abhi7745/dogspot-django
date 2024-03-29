# Generated by Django 4.1.2 on 2024-02-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_map_details_km_distance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="map_details",
            name="km_distance",
            field=models.IntegerField(
                choices=[
                    ("250", "500 Meters"),
                    ("500", "1 Km"),
                    ("1000", "2 Km"),
                    ("1500", "3 Km"),
                    ("2000", "4 Km"),
                    ("2500", "5 Km"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="map_details",
            name="radius_color",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FFD326", "Yellow"),
                    ("#2AAD27", "Green"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="map_details",
            name="radius_color_hexcode",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FFD326", "Yellow"),
                    ("#2AAD27", "Green"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="map_details",
            name="zone",
            field=models.CharField(
                choices=[("red", "Red"), ("yellow", "Yellow"), ("green", "Green")],
                max_length=50,
            ),
        ),
    ]
