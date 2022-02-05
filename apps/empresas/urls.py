from django.urls import path
from .views import EmpresaCreate, EmpresaEdit


urlpatterns = [
    path('create_empresa', EmpresaCreate.as_view(), name='create_empresa'),
    path('edit_empresa/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),

]
