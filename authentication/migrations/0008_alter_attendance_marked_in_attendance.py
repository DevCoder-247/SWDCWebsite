# Generated by Django 5.1.4 on 2025-01-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_secretary_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='marked_IN_attendance',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
