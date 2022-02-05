from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('edit/<int:pk>/', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]
