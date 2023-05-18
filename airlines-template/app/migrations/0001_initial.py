# Generated by Django 4.2.1 on 2023-05-15 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aircraft",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tail_number", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("number_of_seats", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("time_zone", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.FloatField()),
                ("booking_datetime", models.DateTimeField(auto_now_add=True)),
                ("booking_status", models.IntegerField()),
                ("transaction_id", models.IntegerField()),
                ("success_key", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("passport_number", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=255)),
                ("email_address", models.EmailField(max_length=254)),
                ("date_of_birth", models.DateField()),
                ("home_address", models.CharField(max_length=255)),
                ("allergies", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentProvider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("account_id", models.IntegerField()),
                ("username", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seat_number", models.IntegerField()),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.booking"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flight_number", models.CharField(max_length=255)),
                ("duration", models.DurationField()),
                ("departure_datetime", models.DateTimeField()),
                ("price_per_seat", models.IntegerField()),
                ("cost_per_seat", models.IntegerField()),
                (
                    "aircraft",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.aircraft"
                    ),
                ),
                (
                    "departure_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departure_flights",
                        to="app.airport",
                    ),
                ),
                (
                    "destination_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destination_flights",
                        to="app.airport",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="booking",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.customer"
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="flight",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.flight"
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="payment_provider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.paymentprovider"
            ),
        ),
    ]