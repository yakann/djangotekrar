from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import cari_list, cari_detail, CariListesi, CariDetails, GenericCariListesi


urlpatterns = [
    #path('altproje/', views.cari_list),
    path('altproje/', CariListesi.as_view()),
    #path('altproje/<uuid:pk>/', cari_detail),
    path('altproje/<uuid:id>/', CariDetails.as_view()),
    path('altproje/generic/<uuid:id>/', GenericCariListesi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)