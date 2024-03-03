# Generated by Django 4.1.2 on 2024-02-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="map_details",
            name="km_distance",
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="map_details",
            name="radius_color",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="map_details",
            name="radius_color_hexcode",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="map_details",
            name="zone",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]