from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):
    state_choice = (
        ('ABJ', 'Abuja'),
        ('LAG', 'Lagos'),
        ('BEN', 'Benin'),
        ('ANA', 'Anambra'),
        ('ABI', 'Abia'),
        ('PH', 'PortHarcourt'),
        ('KAD', 'Kaduna'),
        ('KNO', 'Kano'),
        ('ADA', 'Adamawa'),
        ('SOK', 'Sokoto'),
        ('CAL', 'Calabar'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))

    feature_choices = (
        ('Motion Sensors', 'Motion Sensors'),
        ('Tracking system', 'Tracking system'),
        ('Auto start/stop', 'Auto start/stop'),
        ('Wind deflector', 'Wind deflector'),
    )

    # door_choices = (
    #     ('2', '2'),
    #     ('4', '4'),
    #     )

    fuel_type_choices = (
        ('petrol', 'petrol'),
        ('battery', 'battery'),
        ('diesel', 'diesel'),
    )
    car_title = models.CharField(max_length=455)
    state = models.CharField(choices=state_choice, max_length=200)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=200)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    car_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    car_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    car_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    car_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    # features = MultiSelectField(choices=feature_choices)
    body_style = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    interior = models.CharField(max_length=200)
    miles = models.IntegerField()
    doors = models.IntegerField()
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=200)
    milage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_type_choices, max_length=200)
    no_of_owners = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_title
