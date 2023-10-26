from django.urls import path
from . import views
urlpatterns=[
             path('cook/' , views.r, name = 'r'),
             
]
