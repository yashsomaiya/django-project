# Generated by Django 4.1.7 on 2023-03-26 03:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactForm",
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
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Sender Name",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("message", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ContactNumber",
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
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Station Phone Number",
                    ),
                ),
                (
                    "emergency_center",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Emergency Center Phone Number",
                    ),
                ),
                (
                    "help_desk",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Help Desk Phone Number",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=122, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Customer",
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
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
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="user name"
                    ),
                ),
                ("feedback", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=122)),
                (
                    "service_type",
                    models.CharField(
                        choices=[
                            ("photo", "Photography"),
                            ("video", "Videography"),
                            ("decor", "Decoration"),
                            ("catering", "Catering"),
                        ],
                        max_length=20,
                    ),
                ),
                ("header", models.CharField(max_length=122)),
                ("desc", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("city", models.CharField(blank=True, default="", max_length=255)),
                ("state", models.CharField(default="", max_length=255)),
                (
                    "featured_package_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("organizer", models.CharField(default="", max_length=122)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="service_images/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WeddingBooking",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=122)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("date_booked", models.DateTimeField(auto_now_add=True)),
                ("location", models.CharField(max_length=200)),
                (
                    "featured_package_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "payment_currency",
                    models.CharField(
                        choices=[("CAD", "CAD"), ("USD", "USD"), ("INR", "INR")],
                        default="CAD",
                        max_length=10,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookingApp.customer",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookingApp.service",
                    ),
                ),
            ],
        ),
    ]
