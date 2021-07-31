# Generated by Django 3.2.3 on 2021-05-14 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0006_alter_productivityperhour_chain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productivityperhour',
            name='chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardMonitoring.chain'),
        ),
        migrations.AlterField(
            model_name='productivityperhour',
            name='hour',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]