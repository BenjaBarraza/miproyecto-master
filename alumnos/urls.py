#from django.conf.urls import url
from django.urls import path
from .views import *



urlpatterns = [
    path('index', index, name='index'),
    path('listadoSQL', listadoSQL, name='listadoSQL'),
    path('crud', crud, name='crud'),
    path('alumnosAdd', alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', alumnosUpdate, name='alumnosUpdate'),

    path('crud_generos', crud_generos, name='crud_generos'),
    path('generosAdd', generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', generos_edit, name='generos_edit'),
    path('menu', menu, name='menu'),




]