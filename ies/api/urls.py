from django.urls import path
from .views import *

urlpatterns=[
    path('validate',validate,name='validate'),
    path('data/',data),
    path('post',postValidate),
    path('test',test)
]
