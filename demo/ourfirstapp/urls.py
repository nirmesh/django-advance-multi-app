from django.conf.urls import url
from ourfirstapp import views

urlpatterns=[
    url("/first/",views.first),
    url("/second/",views.second),
    url("/third/",views.third)
]