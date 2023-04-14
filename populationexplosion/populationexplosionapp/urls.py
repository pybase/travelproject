from . import views
from django.urls import path

urlpatterns = [

    # path('',views.population,name='population'),
    # path('aim/',views.aim,name='aim'),
    # path('dens/',views.dens,name='dens'),
    # path('factors/',views.factors,name='factors')

    path('',views.demo,name='demo')

]
