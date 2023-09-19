from django.urls import path
from . import views


urlpatterns = [
    path('recog/', views.recog, name='recog'),
    path('predict/', views.MLPrediction.as_view(), name='MLPrediction'),
]
