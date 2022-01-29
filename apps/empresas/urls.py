from django.urls import path
from .views import EmpresaCreate


urlpatterns = [
    path('create_empresa', EmpresaCreate.as_view(), name='create_empresa'),

]
