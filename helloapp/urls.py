from django.urls import path
from . import views

urlpatterns=[
  path('myapp/',views.hifirst),
  path('myinfo/',views.myinfo),
  path('myquery/',views.myquery),
]
