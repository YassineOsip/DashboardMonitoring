# Generated by Django 3.2.3 on 2021-05-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0004_alter_chain_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productivityperhour',
            name='hour',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='productivityperhour',
            name='productivity',
            field=models.PositiveIntegerField(),
        ),
    ]
