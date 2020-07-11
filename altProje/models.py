from django.db import models

import uuid

from altProje.yardimcidosya.sabitler import *
# Create your models here.

class Cari(models.Model):

    class Meta:
        db_table = 'Cari'
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    hesapKodu = models.CharField(max_length=20,null=False, blank=False)
    unvan = models.CharField(max_length=80,null=False,blank=False)
    ad = models.CharField(max_length=40,null=True,blank=True)
    soyad = models.CharField(max_length=40,null=True,blank=True)
    aktifPasif = models.IntegerField(null=True,blank=True,choices=AktifPasifType)
    bakGostSekli = models.IntegerField(null=True,blank=True,choices=BakiyeType)
    dvzTL = models.IntegerField(null=True,blank=True,choices=DvzTLType)
    dovizCinsi = models.CharField(max_length=3, null=True,blank=True)
    dovizIslemKurCins = models.IntegerField(null=True,blank=True,choices=DvzKurType)
    krediLimiti = models.IntegerField(null=True,blank=True)
    dvzKrediLimiti = models.IntegerField(null=True,blank=True)
    bolgeKod = models.CharField(max_length=4,null=True,blank=True)
    ozelKod = models.CharField(max_length=20,null=True,blank=True)
    grupKod = models.CharField(max_length=20,null=True,blank=True)
    tipKod = models.CharField(max_length=20,null=True,blank=True)
    mhsKod = models.CharField(max_length=20,null=True,blank=True)
    masrafMerkezi = models.CharField(max_length=20,null=True,blank=True)
    resim=models.ImageField(null=True,blank=True,upload_to = 'Static/pics/cari_pic', default = 'Static/pics/cari_pic/none/no-img.jpg')
    vergiDairesi = models.CharField(max_length=20,null=True,blank=True)
    hesapNo = models.CharField(max_length=20,null=True,blank=True)
    faturaChk = models.CharField(max_length=20,null=True,blank=True)
    iskontoOran=models.IntegerField(null=True,blank=True)
    opsiyonGunu=models.IntegerField(null=True,blank=True)
    odemeGunu=models.IntegerField(null=True,blank=True,choices=OdemeType)
    odemePlani=models.UUIDField(unique=True,default=uuid.uuid4, editable=False,null=True,blank=True,)
    kulSatisFiyat=models.IntegerField(null=True,blank=True,choices=FiyatType)
    chKodu = models.CharField(max_length=20,null=True,blank=True)
    kdvTevfikatUygula=models.BooleanField(null=True,blank=True)
    kdvMuaf=models.BooleanField(null=True,blank=True)
    kdvMuafAck = models.CharField(max_length=20,null=True,blank=True)
    formBaBsUnvan=models.BooleanField(null=True,blank=True)
    sirketEMail = models.EmailField(max_length=50,null=True,blank=True)
    sirketWebAdres = models.CharField(max_length=50,null=True,blank=True)
    satIslemEMail = models.EmailField(max_length=50,null=True,blank=True)
    satAlmaIslemEMail = models.EmailField(max_length=50,null=True,blank=True)
    finIslemEMail = models.EmailField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.unvan


class CariAdres(models.Model):

    class Meta:
        db_table = 'CariAdres'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CariID = models.ForeignKey(Cari, on_delete=models.CASCADE)
    AdresTipi=models.IntegerField(null=True,blank=True)
    AdresBaslik = models.CharField(max_length=50, blank=False, null=False)
    AdresUlkeKod = models.CharField(max_length=20,blank=True, null=True)
    AdresUlkeNumKod = models.CharField(max_length=20,blank=True, null=True)
    AdresSehir = models.CharField(max_length=40,blank=True, null=True)
    AdresIlce = models.CharField(max_length=40,blank=True, null=True)
    AdresKasabaKoy = models.CharField(max_length=40,blank=True, null=True)
    AdresCadde = models.CharField(max_length=40,blank=True, null=True)
    AdresBinaAdi = models.CharField(max_length=40,blank=True, null=True)
    AdresDisKapiNo = models.CharField(max_length=10,blank=True, null=True)
    AdresIcKapiNo = models.CharField(max_length=10,blank=True, null=True)
    AdresPKod = models.CharField(max_length=70,blank=True, null=True)  
   
    def __str__(self):
        return self.AdresBaslik