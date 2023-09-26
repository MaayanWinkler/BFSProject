from django.db import models
from .managers import MeasurementManager

# Create your models here.
class Measurement(models.Model):
    cycle = models.IntegerField()
    diet = models.CharField(max_length=1)
    date = models.DateField()

    temperature = models.FloatField()
    larvae_weight = models.FloatField()
    before_dry = models.FloatField()
    after_dry = models.FloatField()
    
    # objects = MeasurementManager()
    
    def __str__(self):
        return f'Measurement - {self.cycle}, {self.diet}, {self.date}'
