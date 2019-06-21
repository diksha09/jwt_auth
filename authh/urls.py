from django.urls import path
from authh.views import HelloView

urlpatterns = [
    path('home/', HelloView.as_view(), name='hello'),
    ]
