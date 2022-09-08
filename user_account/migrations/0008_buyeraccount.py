# Generated by Django 4.1 on 2022-09-07 11:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_account", "0007_remove_selleraccount_seller_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="BuyerAccount",
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
                ("is_buyer", models.BooleanField(default=True)),
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