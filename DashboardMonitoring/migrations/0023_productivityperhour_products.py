# Generated by Django 3.2.3 on 2021-05-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0022_alter_productivityperhour_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='productivityperhour',
            name='products',
            field=models.ManyToManyField(to='DashboardMonitoring.Product'),
        ),
    ]