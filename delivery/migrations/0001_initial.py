# Generated by Django 5.0.4 on 2024-06-13 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0003_remove_delivery_fk_to_boxpackage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boxpackage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('container_count', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=255, unique=True)),
                ('post_index', models.CharField(default='00-000', max_length=255, unique=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Boxpackage',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pin', models.IntegerField()),
                ('required_capacity', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Package',
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('capacity', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('fk_boxpackage_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.boxpackage')),
            ],
            options={
                'db_table': 'Container',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateTimeField(auto_now_add=True)),
                ('arrival_date', models.DateTimeField()),
                ('pickup_date', models.DateTimeField(null=True)),
                ('size_package', models.CharField(max_length=255, null=True)),
                ('fk_from_boxpackage', models.ForeignKey(blank=True, db_column='fk_from_boxpackage_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.boxpackage')),
                ('fk_to_boxpackage', models.ForeignKey(blank=True, db_column='fk_to_boxpackage_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery_fk_to_boxpackage_set', to='delivery.boxpackage')),
                ('from_user', models.ForeignKey(blank=True, db_column='from_user_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.users')),
                ('to_user_email', models.ForeignKey(blank=True, db_column='to_user_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_email_deliveries', to='crm.users', to_field='email')),
                ('to_user_phone', models.ForeignKey(blank=True, db_column='to_user_phone', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_phone_deliveries', to='crm.users', to_field='phone')),
                ('fk_package', models.OneToOneField(blank=True, db_column='fk_package_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.package')),
            ],
            options={
                'db_table': 'Delivery',
            },
        ),
    ]
