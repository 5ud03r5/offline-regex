# Generated by Django 4.1.7 on 2023-03-29 14:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('regex', '0002_alter_regex_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regex',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bbf84351-9266-4723-ae6d-db54e007301e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
