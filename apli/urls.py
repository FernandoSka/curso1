from django.conf.urls import url
from apli.views import current_datetime
from apli.views import fecha, Registro, Informacion

urlpatterns = [
    url(r'^tiempo/', current_datetime, name="tiempo"),
    url(r'^fecha/$', fecha.as_view(), name='fecha'),    
    url(r'^registro/$', Registro.as_view(), name='Registro'),
    url(r'^listado/$', Informacion.as_view(), name='listado'),

]
