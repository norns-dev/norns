# Generated by Django 4.2.10 on 2024-02-08 17:58

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("parties", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="party",
            managers=[
                ("all_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="partymember",
            managers=[
                ("all_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
