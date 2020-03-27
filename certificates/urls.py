from django.urls import path
from . import views

urlpatterns = [
    path('certificates/',views.certificates,name='certificates'),
    path('addcerti/',views.addcerti,name='addcerti'),
    path('certiadded/',views.certiadded,name='certiadded'),
]
