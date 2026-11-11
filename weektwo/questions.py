# ============================================================
# LECTURE 2 - KALAN ÖNEMLİ PYTHON KOD ŞEKİLLERİ
# ============================================================


# SORU 1
# Bir sayı değişkeni oluştur.
# Sayı 0'dan büyükse karesini hesapla.
# İşlemi if bloğu ve doğru indentation kullanarak gerçekleştir.


# SORU 2
# 1 + 2 + 3 + 4 + 5 + 6 işlemini
# parantez kullanarak birden fazla satıra böl.
# Sonucu ekrana yazdır.


# SORU 3
# Aşağıdaki değerleri tek tek bool() fonksiyonuna gönder:
# 0, -1, "", "Python", [], [0], None
# Sonuçlarını ekrana yazdır.
# Hangi değerlerin falsy olduğunu gözlemle.


# SORU 4
# x = 0 olsun.
# x sıfır olduğunda 10 / x işleminin HİÇ çalışmamasını sağla.
# Bunun için "and" short-circuit davranışını kullan.
# try/except kullanma.


# SORU 5
# 0.1 + 0.2 sonucunu bir değişkende,
# 0.3 değerini başka bir değişkende sakla.
# Önce == ile karşılaştır.
# Daha sonra math.isclose() ile karşılaştır.


# SORU 6
# name, number1 ve number2 adında üç değişken oluştur.
# f-string kullanarak aşağıdakine benzer tek bir metin üret:
# "Ali'nin sayıları 20 ve 30, toplamları 50."


# SORU 7
# range() kullanarak 10, 8, 6, 4, 2 sayılarını
# for döngüsü ile ekrana yazdır.
# Hazır bir liste oluşturma.


# SORU 8
# names = ["Ali", "Ayse", "Mehmet"]
# scores = [80, 95, 70]
#
# zip() kullanarak iki listeyi aynı anda dolaş.
# Her öğrencinin adını ve notunu ekrana yazdır.


# SORU 9
# Bir sayının asal olup olmadığını kontrol et.
# for ... else yapısını kullan.
# Bir bölen bulunursa break çalışsın.
# Döngü break ile bitmezse else kısmı sayının asal olduğunu yazdırsın.


# SORU 10
# 1'den başlayarak while döngüsü oluştur.
# Çift sayıları continue ile atla.
# Bulduğun ilk 5 tek sayıyı bir listeye ekle.
# Liste 5 elemana ulaşınca break ile döngüyü bitir.


# SORU 11
# add_value(values) isminde bir fonksiyon yaz.
# Parametre olarak aldığı listenin içine 100 eklesin.
#
# Fonksiyon dışında bir liste oluştur,
# fonksiyona gönder
# ve fonksiyon çağrısından sonra orijinal listeyi yazdır.
#
# Mutable bir nesnenin fonksiyona gönderildiğinde davranışını incele.


# SORU 12
# increment(number) isminde bir fonksiyon yaz.
# Fonksiyon içinde number değerini 1 artır ve yazdır.
#
# Fonksiyon dışında number = 10 benzeri bir integer oluştur.
# Fonksiyona gönder.
# Fonksiyon çağrısından sonra dışarıdaki değeri tekrar yazdır.
#
# Immutable nesnenin davranışını gözlemle.


# SORU 13
# triangle_area(base, height) isminde bir fonksiyon yaz.
# base veya height negatifse ValueError raise et.
# İkisi de geçerliyse üçgen alanını return et.


# SORU 14
# Bir önceki triangle_area fonksiyonunu
# negatif bir değerle try bloğu içerisinde çağır.
#
# ValueError oluşursa except ValueError as error:
# şeklinde hatayı yakala ve hata mesajını yazdır.


# SORU 15
# power(base, exp=2) isminde bir fonksiyon yaz.
#
# 1) Sadece base göndererek çağır.
# 2) base ve exp göndererek çağır.
# 3) Parametreleri sırasını değiştirerek keyword argument ile çağır.
#
# Örneğin fonksiyonun çağrısında exp ve base isimlerini açıkça kullan.


# SORU 16
# add_item(item, items=None) isminde bir fonksiyon yaz.
#
# Eğer items None ise fonksiyon içerisinde yeni boş liste oluştur.
# item değerini listeye ekle ve listeyi döndür.
#
# Fonksiyonu iki kez sadece item göndererek çağır.
# İki çağrının aynı listeyi paylaşmamasını sağla.


# SORU 17
# summarize(*args, **kwargs) isminde bir fonksiyon yaz.
#
# args değerini ve kwargs değerini ayrı ayrı yazdır.
#
# Fonksiyonu şu tarzda çağır:
# birkaç positional değer
# ve birkaç named/keyword değer gönder.
#
# Ayrıca type(args) ve type(kwargs) değerlerini yazdır.


# SORU 18
# nums = [1, 2, 3, 4] listesi için:
#
# lambda + map kullanarak sayıların karelerini oluştur.
# lambda + filter kullanarak sadece çift sayıları seç.
# sorted ve lambda key kullanarak sayıları büyükten küçüğe sırala.
#
# Her işlemden sonra orijinal nums listesinin değişip değişmediğini kontrol et.


# SORU 19
# factorial(n) isminde bir fonksiyon yaz.
# Negatif n verilirse ValueError raise et.
# Değilse factorial değerini for döngüsüyle hesapla.
#
# Daha sonra:
# factorial(3) == 6
# koşulunu assert ile test et.
#
# Fonksiyonun docstring'ine ayrıca factorial(0) ve factorial(5)
# için doctest örnekleri ekle.


# SORU 20
# is_harshad_number(n) isminde bir fonksiyon yaz.
#
# Önce n'nin int olup olmadığını isinstance() ile kontrol et.
# n pozitif değilse False döndür.
#
# Sayının rakamlarını STRING'E ÇEVİRMEDEN topla.
#
# Son basamağı almak için % kullan.
# Son basamağı sayıdan silmek için // kullan.
#
# Sayı rakamları toplamına tam bölünüyorsa True,
# bölünmüyorsa False döndür.
#
# Örnek olarak:
# 18, 15, 156, 0 ve 18.0 değerleriyle fonksiyonu test et.