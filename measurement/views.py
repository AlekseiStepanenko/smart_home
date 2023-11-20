# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import serializers

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class ListCreateAPIView(ListAPIView):
    """Добавить измерение. Указываются ID датчика и температура"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'Измерение добавлено'})


class RetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """Получить информацию по конкретному датчику."""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



class CreateAPIView(ListAPIView):
    """Создать датчик. Указываются название и описание датчика."""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class ListView(ListAPIView):
    """Получить список датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
