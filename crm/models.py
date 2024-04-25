
from django.db import models



class Boxpackage(models.Model):
    id = models.BigAutoField(primary_key=True)
    count_container = models.IntegerField()
    size = models.CharField()
    location = models.CharField(unique=True)

    class Meta:
        db_table = 'Boxpackage'


class Container(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField(unique=True)
    capacity = models.CharField()
    fk_boxpackage = models.ForeignKey(Boxpackage, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'Container'

class Package(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField(unique=True)
    pin = models.IntegerField()
    status = models.CharField()

    class Meta:
        db_table = 'Package'


class Users(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    phone = models.CharField(unique=True)
    email = models.CharField(unique=True)
    password = models.CharField()

    class Meta:
        db_table = 'Users'


class Delivery(models.Model):
    fk_package_number = models.OneToOneField('Package', models.DO_NOTHING, db_column='fk_package_number', blank=True, null=True)
    fk_from_container_num = models.ForeignKey(Container, models.DO_NOTHING, db_column='fk_from_container_num', to_field='number', blank=True, null=True)
    fk_to_container_num = models.ForeignKey(Container, models.DO_NOTHING, db_column='fk_to_container_num', to_field='number', related_name='delivery_fk_to_container_num_set', blank=True, null=True)
    fk_from_boxpackage_location = models.ForeignKey(Boxpackage, models.DO_NOTHING, db_column='fk_from_boxpackage_location', to_field='location', blank=True, null=True)
    fk_to_boxpackage_location = models.ForeignKey(Boxpackage, models.DO_NOTHING, db_column='fk_to_boxpackage_location', to_field='location', related_name='delivery_fk_to_boxpackage_location_set', blank=True, null=True)
    fk_users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    data_departure = models.DateTimeField()
    data_receiving = models.DateTimeField()

    class Meta:
        db_table = 'Delivery'
