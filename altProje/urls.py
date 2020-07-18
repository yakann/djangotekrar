from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import cari_list, cari_detail, CariListesi, CariDetails, GenericCariListesi, CariViewSet, CariGenericViewSet, CariModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('cariler', CariViewSet, basename='cariler')
#router.register('cariler', CariGenericViewSet, basename='cariler')
router.register('cariler', CariModelViewSet, basename='cariler')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<uuid:pk>/', include(router.urls)),

    #path('altproje/', views.cari_list),
    path('altproje/', CariListesi.as_view()),
    #path('altproje/<uuid:pk>/', cari_detail),
    path('altproje/<uuid:id>/', CariDetails.as_view()),
    path('altproje/generic/<uuid:id>/', GenericCariListesi.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)