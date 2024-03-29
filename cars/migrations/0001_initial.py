# Generated by Django 3.0.7 on 2022-06-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=455)),
                ('state', models.CharField(choices=[('ABJ', 'Abuja'), ('LAG', 'Lagos'), ('BEN', 'Benin'), ('ANA', 'Anambra'), ('ABI', 'Abia'), ('PH', 'PortHarcourt'), ('KAD', 'Kaduna'), ('KNO', 'Kano'), ('ADA', 'Adamawa'), ('SOK', 'Sokoto'), ('CAL', 'Calabar')], max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('condition', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('car_photo', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('features', models.CharField(choices=[('Motion Sensors', 'Motion Sensors'), ('Tracking system', 'Tracking system'), ('Auto start/stop', 'Auto start/stop'), ('Wind deflector', 'Wind deflector')], max_length=700)),
                ('body_style', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('transmission', models.CharField(max_length=200)),
                ('interior', models.CharField(max_length=200)),
                ('miles', models.IntegerField()),
                ('doors', models.IntegerField(choices=[('2', '2'), ('4', '4')])),
                ('passengers', models.IntegerField()),
                ('vin_no', models.CharField(max_length=200)),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(choices=[('petrol', 'petrol'), ('battery', 'battery'), ('diesel', 'diesel')], max_length=200)),
                ('no_of_owners', models.CharField(max_length=200)),
                ('is_featured', models.BooleanField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
