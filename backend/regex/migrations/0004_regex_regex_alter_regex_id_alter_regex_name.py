# Generated by Django 4.1.7 on 2023-03-29 15:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('regex', '0003_alter_regex_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='regex',
            name='regex',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='regex',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f5d3da5e-3360-4a71-9765-b24e5710e1ad'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='regex',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]