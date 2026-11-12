# ============================================================
# 1) == ve is FARKI
# ============================================================

print("----- == ve is -----")

list_a = [1, 2, 3]
list_b = [1, 2, 3]

# == değerlerin eşit olup olmadığına bakar
print(list_a == list_b)     # True

# is aynı nesne olup olmadığına bakar
print(list_a is list_b)     # False

# Değerleri aynı ama bellekte farklı iki liste nesnesidir.

print(id(list_a))
print(id(list_b))


# ============================================================
# 2) MUTABLE
# ============================================================

print("\n----- Mutable -----")

# Mutable = Değiştirilebilir
# Bir nesnenin oluşturulduktan sonra
# aynı nesne olarak değiştirilebilir olmasıdır.

# Mutable örnekleri:
# list
# dict
# set

mutable_list = [1, 2, 3, 4]

print("İlk hali:", mutable_list)
print("İlk id:", id(mutable_list))

mutable_list.append(5)

print("Yeni hali:", mutable_list)
print("Son id:", id(mutable_list))

# append() mevcut listeyi değiştirdi.
# Yeni bir liste oluşturulmadığı için id aynı kalır.


# ============================================================
# 3) IMMUTABLE
# ============================================================

print("\n----- Immutable -----")

# Immutable = Değiştirilemez

# Immutable örnekleri:
# int
# float
# bool
# str
# tuple
# frozenset

immutable_number = 10

print("İlk değer:", immutable_number)
print("İlk id:", id(immutable_number))

immutable_number += 1

print("Yeni değer:", immutable_number)
print("Son id:", id(immutable_number))

# 10 nesnesi 11'e dönüştürülmedi.
# Yeni bir int nesnesi oluştu.
# immutable_number artık yeni nesneyi gösteriyor.


# ============================================================
# 4) IMMUTABLE NESNEDE İKİ REFERANS
# ============================================================

print("\n----- Immutable Referans Örneği -----")

number_one = 100
number_two = number_one

print(id(number_one))
print(id(number_two))
print(number_one is number_two)     # True

number_two = number_two + 1

# 100 nesnesi değişmedi.
# number_two artık yeni 101 nesnesini gösteriyor.

print("number_one:", number_one)
print("number_two:", number_two)

print(id(number_one))
print(id(number_two))
print(number_one is number_two)     # False


# ============================================================
# 5) ALIASING
# ============================================================

print("\n----- Aliasing -----")

original_list = [1, 2, 3]

alias_list = original_list

# Burada kopya oluşturulmadı.
# İki değişken aynı listeyi gösteriyor.

print(original_list is alias_list)     # True

alias_list.append(5)

print("original_list:", original_list)
print("alias_list:", alias_list)

# İkisi de:
# [1, 2, 3, 5]

# Çünkü aynı liste nesnesini gösteriyorlar.


# ============================================================
# 6) ALIAS vs SHALLOW COPY vs DEEP COPY
# ============================================================

print("\n----- Copy -----")

import copy

copy_original = [1, 2, 3]

copy_alias = copy_original
copy_shallow = copy_original.copy()
copy_deep = copy.deepcopy(copy_original)

copy_original.append(4)

print("original:", copy_original)
print("alias:", copy_alias)
print("shallow:", copy_shallow)
print("deep:", copy_deep)

# original: [1, 2, 3, 4]
# alias:    [1, 2, 3, 4]
# shallow:  [1, 2, 3]
# deep:     [1, 2, 3]


# ============================================================
# 7) SHALLOW COPY - NESTED LIST
# ============================================================

print("\n----- Shallow Copy Nested List -----")

nested_original = [[1, 2], [3, 4]]

nested_shallow = nested_original.copy()

nested_shallow[0].append(99)

print("original:", nested_original)
print("shallow:", nested_shallow)

# original: [[1, 2, 99], [3, 4]]
# shallow:  [[1, 2, 99], [3, 4]]

# Neden?
#
# Dış liste kopyalandı.
# Ama iç listeler kopyalanmadı.
#
# İki dış liste aynı iç liste nesnelerini gösteriyor.


# ============================================================
# 8) SHALLOW COPY - ID KONTROLÜ
# ============================================================

print("\n----- Shallow Copy ID Kontrol -----")

shallow_original = [[10, 20], [30, 40]]
shallow_copy = shallow_original.copy()

print("Dış listelerin id değerleri:")

print(id(shallow_original))
print(id(shallow_copy))

# Farklı olmalı.
# Çünkü dış liste kopyalandı.


print("İlk iç listelerin id değerleri:")

print(id(shallow_original[0]))
print(id(shallow_copy[0]))

# Aynı olmalı.
# Çünkü shallow copy iç nesneleri kopyalamaz.


print(
    "Dış liste aynı mı?",
    shallow_original is shallow_copy
)

print(
    "İç liste aynı mı?",
    shallow_original[0] is shallow_copy[0]
)


# ============================================================
# 9) DEEP COPY
# ============================================================

print("\n----- Deep Copy -----")

deep_original = [[1, 2], [3, 4]]

deep_copy = copy.deepcopy(deep_original)

deep_copy[0].append(42)

print("original:", deep_original)
print("deep copy:", deep_copy)

# original:
# [[1, 2], [3, 4]]

# deep copy:
# [[1, 2, 42], [3, 4]]

# deepcopy iç nesneleri de kopyaladığı için
# original etkilenmez.


# ============================================================
# 10) DEEP COPY - ID KONTROLÜ
# ============================================================

print("\n----- Deep Copy ID Kontrol -----")

deep_id_original = [[5, 6], [7, 8]]

deep_id_copy = copy.deepcopy(deep_id_original)

print("Dış listelerin id değerleri:")

print(id(deep_id_original))
print(id(deep_id_copy))

print("İç listelerin id değerleri:")

print(id(deep_id_original[0]))
print(id(deep_id_copy[0]))

# Hem dış hem iç nesnelerin id değerleri farklıdır.

print(
    "Dış liste aynı mı?",
    deep_id_original is deep_id_copy
)

print(
    "İç liste aynı mı?",
    deep_id_original[0] is deep_id_copy[0]
)


# ============================================================
# 11) MULTIPLE ASSIGNMENT İLE ALIASING
# ============================================================

print("\n----- Multiple Assignment Aliasing -----")

first_list = second_list = [1, 2, 3]

second_list.append(5)

print("first_list:", first_list)
print("second_list:", second_list)

print(first_list is second_list)     # True

# first_list ve second_list
# aynı liste nesnesini gösteriyor.


# ============================================================
# 12) MULTIPLE ASSIGNMENT VE SWAP
# ============================================================

print("\n----- Swap -----")

num_one = 1
num_two = 2

print("Önce:", num_one, num_two)

num_one, num_two = num_two, num_one

print("Sonra:", num_one, num_two)

# Geçici bir üçüncü değişken kullanmadan
# değerleri yer değiştirdik.


# ============================================================
# 13) TUPLE IMMUTABLE AMA İÇİNDE MUTABLE NESNE OLABİLİR
# ============================================================

print("\n----- Tuple ve Mutable İç Nesne -----")

tuple_example = ([1, 2], [3, 4])

print("İlk hali:", tuple_example)

tuple_example[0].append(5)

print("Son hali:", tuple_example)

# Çıktı:
# ([1, 2, 5], [3, 4])

# Tuple immutable'dır.
# Yani tuple içerisindeki referansları değiştiremeyiz.

# Fakat tuple'ın içindeki liste mutable olduğu için
# listenin kendisini değiştirebiliriz.


# Örneğin aşağıdaki işlem yapılamaz:

# tuple_example[0] = [10, 20]

# TypeError verir.
# Çünkü burada tuple'ın elemanını başka bir nesneyle
# değiştirmeye çalışıyoruz.
