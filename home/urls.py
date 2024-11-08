from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert_data, name='insert'),
    path('deletar_pessoa/<int:id>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('caminhoneiro_index', views.caminhoneiro_index, name='caminhoneiro_index'),
    path('adiciona_caminhoneiro', views.adiciona_caminhoneiro, name='adiciona_caminhoneiro'),
    path('deletar_caminhoneiro/<int:id>', views.deletar_caminhoneiro, name='deletar_caminhoneiro')

]
