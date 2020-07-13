from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Rest Api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Cari,CariAdres
from .serializers import CariSerializer, CariAdresSerializer

class CariListesi(APIView):

    def get(self, request):
            cariler = Cari.objects.all()
            serializer = CariSerializer(cariler, many=True)
            return  Response(serializer.data)
    def post(self):
            pass

class CariAdresListesi(viewsets.ModelViewSet):

    queryset = CariAdres.objects.all()
    serializer_class = CariAdresSerializer

"""
Viewsets’den bahsetmek gerekirse, DRF ile oluşturmuş olduğumuz API’lara yapılan istekler sonucunda, hangi model, 
hangi istek tipine ne cevap vericek bunların ayarlamasını yapmamız gerekmektedir. Manuel olarak bu işlemleri gerçekleştirmek 
yerine viewsets sınıfı ile bütün bu yapılması gerekenleri DRF bizim yerimize gerçekleştirir. Biz en basit haliyle ModelViewSet 
sınıfını kullanacağız. Bu sınıf , karmaşık model yapıları üzerinde yapılacak işlemler için hazır fonksiyonlar oluşturur. 
list(),retrieve(),create(),update(),destroy() gibi fonksiyonlar bu sınıf içerisinde erişim sağlayabileceğimiz varsayılan yapılardır. 
Dilersek bu metotları kendimize göre düzenleyebiliriz.Yaptığmız uygulamanın ölçeğine, veriler üzerinde yapacağımız değişikliklere göre 
tek bir serileştirilmiş model için birden fazla View tanımlamamız mümkündür.
"""