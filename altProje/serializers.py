from rest_framework import serializers

from .models import Cari, CariAdres


class CariSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cari
        fields = ('unvan', 'ad', 'soyad')

class CariAdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CariAdres
        fields = ('CariID', 'AdresBaslik', 'AdresUlkeKod')

"""
Serializers.HyperlinkedModelSerializer = bu serileştirme yöntemi DRF de en çok tercih edilen serileştirme yöntemlerinden biridir. 
Eğer çok ilişkili yapılara sahip modelleriniz varsa bu yöntemi kullanmanızı tavsiye ederim. Kısaca anlatmak gerekirse, bu yöntem 
ile modelin ilişkili olduğu diğer yapılar eğer serileştirilecek alanlar arasında yer alıyor ise , ilişkili modellerdeki verilerin 
bağlantısı geri dönen veri içerisinde yer alır.

"""