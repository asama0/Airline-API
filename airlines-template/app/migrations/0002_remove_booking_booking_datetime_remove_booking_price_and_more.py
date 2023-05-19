# Generated by Django 4.2.1 on 2023-05-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="booking", name="booking_datetime",),
        migrations.RemoveField(model_name="booking", name="price",),
        migrations.RemoveField(model_name="booking", name="success_key",),
        migrations.AlterField(
            model_name="booking",
            name="booking_status",
            field=models.CharField(
                choices=[(1, "on_hold "), (2, "confirmed"), (3, "cancelled")],
                default="on_hold",
                max_length=255,
            ),
        ),
    ]