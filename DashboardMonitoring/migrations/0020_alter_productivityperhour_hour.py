# Generated by Django 3.2.3 on 2021-05-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0019_alter_productivityperhour_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productivityperhour',
            name='hour',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
