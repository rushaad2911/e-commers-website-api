# Generated by Django 4.1 on 2022-09-07 06:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SellerAccount",
            fields=[
                (
                    "useraccount_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("is_seller", models.BooleanField()),
                ("shop_name", models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("user_account.useraccount",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
