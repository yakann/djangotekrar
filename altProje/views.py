from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Rest Api
# from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt

from .serializers import CariSerializer, CariAdresSerializer
from .models import Cari,CariAdres

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from django.shortcuts import get_object_or_404
#VIEWSET AND ROUTERS
class CariViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Cari.objects.all()
        serializer = CariSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CariSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Cari.objects.all()
        cariler = get_object_or_404(queryset, pk=pk)
        serializer = CariSerializer(cariler)
        return Response(serializer.data)

    def update(self, request, pk=None):
        cari = CariListesi.objects.get(pk=pk)
        serializer = CariSerializer(cari, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


#GENERİC VIEWS and AUTHENTICATION

class GenericCariListesi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = CariSerializer
    queryset = Cari.objects.all()
    lookup_field = 'id'
    
    #authentication_classes=[SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request, id=None):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

#CLASS BASED VIEW
class CariListesi(APIView):

    def get(self, request):
            queryset = Cari.objects.all()
            serializer = CariSerializer(queryset, many=True)
            return Response(serializer.data)
    def post(self, request):
            serializer = CariSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CariDetails(APIView):

    def get_object(self, id):
        try:
            return Cari.objects.get(id=id)
        except Cari.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        cari = self.get_object(id)
        serializer = CariSerializer(cari)
        return Response(serializer.data)

    def put(self, request):
        cari = self.get_object(id)
        serializer = CariSerializer(cari, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        cari = self.get_object(id)
        cari.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#FUNCTION BASED VİEW
@api_view(['GET', 'POST'])
@csrf_exempt
def cari_list(request, format=None):

    if request.method == 'GET':
        queryset = Cari.objects.all()
        serializer = CariSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CariSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def cari_detail(request, pk, format=None):

    try:
        cari = Cari.objects.get(pk=pk)
    except Cari.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CariSerializer(cari)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CariSerializer(cari, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cari.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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