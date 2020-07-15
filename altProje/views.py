from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Rest Api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


from django.views.decorators.csrf import csrf_exempt

from .serializers import CariSerializer, CariAdresSerializer
from .models import Cari,CariAdres
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def cari_list(request):

    if request.method == 'GET':
        queryset = Cari.objects.all()
        serializer = CariSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CariSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def cari_detail(request, pk):

    try:
        cari = Cari.objects.get(pk=pk)
    except Cari.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CariSerializer(cari)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CariSerializer(cari, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cari.delete()
        return HttpResponse(status=204)


"""class CariListesi(APIView):

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

"""
Viewsets’den bahsetmek gerekirse, DRF ile oluşturmuş olduğumuz API’lara yapılan istekler sonucunda, hangi model, 
hangi istek tipine ne cevap vericek bunların ayarlamasını yapmamız gerekmektedir. Manuel olarak bu işlemleri gerçekleştirmek 
yerine viewsets sınıfı ile bütün bu yapılması gerekenleri DRF bizim yerimize gerçekleştirir. Biz en basit haliyle ModelViewSet 
sınıfını kullanacağız. Bu sınıf , karmaşık model yapıları üzerinde yapılacak işlemler için hazır fonksiyonlar oluşturur. 
list(),retrieve(),create(),update(),destroy() gibi fonksiyonlar bu sınıf içerisinde erişim sağlayabileceğimiz varsayılan yapılardır. 
Dilersek bu metotları kendimize göre düzenleyebiliriz.Yaptığmız uygulamanın ölçeğine, veriler üzerinde yapacağımız değişikliklere göre 
tek bir serileştirilmiş model için birden fazla View tanımlamamız mümkündür.
"""