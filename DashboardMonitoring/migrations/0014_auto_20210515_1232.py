# Generated by Django 3.2.3 on 2021-05-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardMonitoring', '0013_auto_20210515_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='productivityperhour',
            name='hourRef',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='ref',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productivityperhour',
            name='hour',
            field=models.PositiveIntegerField(),
        ),
    ]
