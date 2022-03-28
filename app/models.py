from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class UserModel(models.Model):
    image = models.FileField(upload_to='images', default='default.jpg', blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    bloodgrp = models.CharField(max_length=50, null=True, blank=True)
    STANDARDS = (
        ('', 'Select'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    standard = models.CharField(max_length=100, null=True, blank=True, choices=STANDARDS)
    CLASSES = (
        ('', 'Select'),
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    classs = models.CharField(max_length=100, null=True, blank=True, choices=CLASSES)

    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS, null=True, default=None)
    address = models.TextField(null=True, blank=True)
    HOBIES = (
        ('Reading', 'Reading'),
        ('Writing', 'Writing'),
        ('Dancing', 'Dancing'),
        ('Singing', 'Singing'),
        ('Playing', 'Playing'),

    )
    hobby = MultiSelectField(max_length=150, null=True, blank=True, choices=HOBIES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
