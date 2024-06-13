from django.db import models


#paczkomat
class Boxpackage(models.Model):
    id = models.BigAutoField(primary_key=True)
    container_count = models.IntegerField(null=True) # liczba cointenerow 
    location = models.CharField(unique=True, max_length=255) # dlugosc szerokosc 
    post_index = models.CharField(unique=True, max_length=255, default='00-000') # index pocztowy 
    description = models.CharField(max_length=255, null=True) # ulica budunek etc

    class Meta:
        db_table = 'Boxpackage'

#komorka paczkomatu
class Container(models.Model):
    id = models.BigAutoField(primary_key=True)
    capacity = models.CharField(max_length=255)
    fk_boxpackage_id = models.ForeignKey(Boxpackage, models.DO_NOTHING, blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        db_table = 'Container'

class Package(models.Model):
    id = models.BigAutoField(primary_key=True)
    pin = models.IntegerField()
    required_capacity = models.CharField(max_length=255, null=True) # to samo co capacity w kontenerie w paczkomacie
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'Package'




class Delivery(models.Model):
    fk_package = models.OneToOneField(Package, models.DO_NOTHING, db_column='fk_package_id', blank=True, null=True)
    fk_from_boxpackage = models.ForeignKey(Boxpackage, models.DO_NOTHING, db_column='fk_from_boxpackage_id', blank=True, null=True)
    fk_to_boxpackage = models.ForeignKey(Boxpackage, models.DO_NOTHING, db_column='fk_to_boxpackage_id', related_name='delivery_fk_to_boxpackage_set', blank=True, null=True)
    departure_date = models.DateTimeField(auto_now_add=True)  # Automatically set to the current time when the delivery is created
    arrival_date = models.DateTimeField()  # +2 days from departure_date
    pickup_date = models.DateTimeField(null=True)  # changes when user makes POST on /api/delivery/receive to get package
    from_user = models.ForeignKey(Users, models.DO_NOTHING, db_column='from_user_id', blank=True, null=True)
    to_user_phone = models.ForeignKey(Users, models.DO_NOTHING, db_column='to_user_phone', to_field='phone', related_name='user_phone_deliveries', blank=True, null=True)
    to_user_email = models.ForeignKey(Users, models.DO_NOTHING, db_column='to_user_email', to_field='email', related_name='user_email_deliveries', blank=True, null=True)
    size_package = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'Delivery'

