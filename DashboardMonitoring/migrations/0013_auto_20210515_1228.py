# Generated by Django 3.2.3 on 2021-05-15 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0012_auto_20210515_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productivityperhour',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='chain',
        ),
        migrations.AddField(
            model_name='product',
            name='chain',
            field=models.ManyToManyField(to='DashboardMonitoring.Chain'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='productivityperhour',
            name='chain',
        ),
        migrations.AddField(
            model_name='productivityperhour',
            name='chain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DashboardMonitoring.chain'),
        ),
    ]
