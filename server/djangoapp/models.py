# Uncomment the following imports before adding the Model codee

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    CAR_TYPES = [
    ('SEDAN', 'Sedan'),
    ('SUV', 'SUV'),
    ('WAGON', 'Wagon'),
    ('HATCHBACK', 'Hatchback'),
    ('COUPE', 'Coupe'),
    ('MINIVAN', 'Minivan'),
    ('CONVERTIBLE', 'Convertible'),
    ('PICKUP', 'Pickup Truck'),
    ('CROSSOVER', 'Crossover'),
    ('SPORTS', 'Sports Car'),
    ('LUXURY', 'Luxury Car'),
    ('MUSCLE', 'Muscle Car'),
    ('ROADSTER', 'Roadster'),
    ('OFFROAD', 'Off-Road Vehicle'),
    ('SUPER', 'Supercar'),
    ('ELECTRIC', 'Electric Vehicle (EV)'),
    ('HYBRID', 'Hybrid Car'),
    ('COMMERCIAL', 'Commercial Vehicle'),
    ('CLASSIC', 'Classic/Vintage Car'),
]

    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2025),
            MinValueValidator(2015),
        ]
    )

    def __str__(self):
        return self.name