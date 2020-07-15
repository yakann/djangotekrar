from django.urls import path

from .views import cari_list, cari_detail


urlpatterns = [
    path('altproje/', cari_list),
    path('altproje/<uuid:pk>/', cari_detail),
]