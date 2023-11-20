from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Датчик')
    description = models.CharField(max_length=90, verbose_name='Описание')


class Measurement(models.Model):
    id = models.ForeignKey(Sensor, primary_key=True, on_delete=models.CASCADE, related_name='measurements')
    temp = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Температура')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
