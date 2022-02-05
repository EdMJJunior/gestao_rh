from django.urls import path
from .views import DocumetoCreate

urlpatterns = [
    path('create/<int:funcionario_id>/', DocumetoCreate.as_view(), name='create_documento'),

]
