from django.urls import path

from measurement.views import ListCreateAPIView, RetrieveUpdateAPIView, ListView, CreateAPIView

urlpatterns = [
    path('sensors/', CreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('list/', ListView.as_view()),
    path('measurements/', ListCreateAPIView.as_view()),
]
