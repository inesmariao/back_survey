from django.urls import path
from . import views

urlpatterns = [
    path('api/monedas/', views.MonedaListCreate.as_view(), name='moneda-list-create'),
    path('api/monedas/<int:pk>/', views.MonedaRetrieveUpdateDestroy.as_view(), name='moneda-detail'),

]
