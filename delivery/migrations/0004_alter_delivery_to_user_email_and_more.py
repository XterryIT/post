# Generated by Django 5.0.4 on 2024-06-16 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_remove_delivery_pickup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='to_user_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='to_user_phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
