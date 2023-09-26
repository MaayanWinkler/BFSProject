from django.db import models

class MeasurementManager(models.Manager):
    def create(self, cycle, diet, date,temperature,larvae_weight,before_dry,after_dry):
        measure = self.create()
        measure.cycle = cycle
        measure.diet = diet
        measure.date = date
        measure.temperature = temperature
        measure.larvae_weight = larvae_weight
        measure.before_dry = before_dry
        measure.after_dry = after_dry
        measure.save()
        return measure
