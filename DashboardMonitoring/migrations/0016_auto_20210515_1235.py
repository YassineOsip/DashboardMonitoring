# Generated by Django 3.2.3 on 2021-05-15 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0015_alter_productivityperhour_hourref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productivityperhour',
            name='hourRef',
        ),
        migrations.AlterField(
            model_name='productivityperhour',
            name='chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DashboardMonitoring.chain'),
        ),
    ]
