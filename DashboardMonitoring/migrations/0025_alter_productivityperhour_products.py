# Generated by Django 3.2.3 on 2021-05-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0024_alter_productivityperhour_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productivityperhour',
            name='products',
            field=models.ManyToManyField(blank=True, to='DashboardMonitoring.Product'),
        ),
    ]