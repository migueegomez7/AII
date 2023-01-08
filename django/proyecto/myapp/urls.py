from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('carga/',v.populateDatabase),
    path('seleccion/',v.seleccion),
    path('indice/',v.indice)
]