# Generated by Django 5.0.4 on 2024-06-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_delivery_fk_to_boxpackage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_register',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
