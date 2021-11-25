from django.db import models
from ckeditor.fields import RichTextField


class Person(models.Model):
    manufacturers = [
        ('Covaxin', 'Covaxin (Bharat Biotech)'),
        ('Covishield', 'Covishield (Serum Institute of India)'),
        ('Sputnik', 'Sputnik V'),
    ]
    doses = [
        ('1st', 'First Dose'),
        ('2nd', 'Second Dose'),
    ]

    name = models.CharField(max_length=500, verbose_name='First Name')
    fname = models.CharField(max_length=500, verbose_name="Father's Name")
    lname = models.CharField(max_length=500, verbose_name="Surname")
    dob = models.DateField(auto_now_add=False, verbose_name='Date of Birth')
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    manufacturers = models.CharField(max_length=50, choices=manufacturers)
    doses = models.CharField(max_length=50, choices=doses)
    dov = models.DateField(auto_now_add=False, verbose_name='Date of Vaccination')

    def __str__(self):
        return self.name + " " + self.lname
