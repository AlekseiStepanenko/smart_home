# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from measurement.models import Sensor
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sensor = Sensor()
        sensor.name = request.data.get('name')
        sensor.description = request.data.get('description')
        sensor.save()
        return Response({
            'message': f'Датчик "{sensor.name}" создан'
        })


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
