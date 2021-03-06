# Generated by Django 3.0.7 on 2020-06-14 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeoPoint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=10, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=11, null=True
                    ),
                ),
                (
                    "street_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("route", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "neighborhood",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("political", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "administrative_area_level_1",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "administrative_area_level_2",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                "ordering": ["-created", "-modified"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
    ]
