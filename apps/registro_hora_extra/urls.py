from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraEdit,
                    HoraExtraDelete,
                    HoraExtraCreate,
                    HoraExtraEditBase,
                    UtilizouHoraExtra
                    )


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('edit-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='edit_hora_extra_funcionario'),
    path('edit/<int:pk>/', HoraExtraEditBase.as_view(), name='edit_hora_extra'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]
