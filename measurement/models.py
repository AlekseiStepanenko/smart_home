from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=90)


class Measurement(models.Model):
    id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temp = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
