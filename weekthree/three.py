# ============================================================
# LECTURE 3 - PYTHON FUNDAMENTALS II
# ============================================================


# ============================================================
# 1) LIST / TUPLE / DICT / SET KISA TEKRAR
# ============================================================

print("----- Container Recap -----")

recap_list = [1, 2, 3]               # ordered, mutable
recap_tuple = (1, 2, 3)              # ordered, immutable
recap_dict = {"name": "Ali"}          # key-value, mutable
recap_set = {1, 2, 3}                 # unique values, mutable

print(recap_list)
print(recap_tuple)
print(recap_dict)
print(recap_set)


# ============================================================
# 2) SLICING
# ============================================================

print("\n----- Slicing -----")

slice_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Yapı:
# sequence[start:stop:step]

# start dahil
# stop dahil değil

print(slice_numbers[1:4])
# [2, 3, 4]

print(slice_numbers[:3])
# [1, 2, 3]

print(slice_numbers[5:])
# [6, 7, 8]

print(slice_numbers[::2])
# [1, 3, 5, 7]

print(slice_numbers[::-1])
# [8, 7, 6, 5, 4, 3, 2, 1]

print(slice_numbers[-3:])
# [6, 7, 8]


# ============================================================
# 3) LIST SLICING SHALLOW COPY ÜRETİR
# ============================================================

print("\n----- Slicing Copy -----")

slice_original = [1, 2, 3]

slice_copy = slice_original[:]

print(slice_original)
print(slice_copy)

print(slice_original is slice_copy)
# False

slice_copy[0] = 100

print(slice_original)
# [1, 2, 3]

print(slice_copy)
# [100, 2, 3]

# List slicing yeni bir dış liste üretir.
# Yani shallow copy mantığı vardır.


# ============================================================
# 4) UNPACKING
# ============================================================

print("\n----- Unpacking -----")

unpack_point = (3.0, 4.0)

point_x, point_y = unpack_point

print(point_x)
print(point_y)

# Tuple içindeki değerleri iki değişkene dağıttık.


# ============================================================
# 5) STARRED UNPACKING
# ============================================================

print("\n----- Starred Unpacking -----")

unpack_numbers = [10, 20, 30, 40]

first_value, *rest_values = unpack_numbers

print(first_value)
# 10

print(rest_values)
# [20, 30, 40]


*head_values, last_value = unpack_numbers

print(head_values)
# [10, 20, 30]

print(last_value)
# 40


# * ile yakalanan kısım LIST olur.


# ============================================================
# 6) STARRED UNPACKING ORTADA
# ============================================================

print("\n----- Middle Unpacking -----")

middle_numbers = [1, 2, 3, 4, 5]

middle_first, *middle_values, middle_last = middle_numbers

print(middle_first)
# 1

print(middle_values)
# [2, 3, 4]

print(middle_last)
# 5


# ============================================================
# 7) STRING UNPACKING
# ============================================================

print("\n----- String Unpacking -----")

word_value = "python"

word_first, *word_middle, word_last = word_value

print(word_first)
# p

print(word_middle)
# ['y', 't', 'h', 'o']

print(word_last)
# n


# ============================================================
# 8) DICT.ITEMS() İLE UNPACKING
# ============================================================

print("\n----- Dict Items Unpacking -----")

student_info = {
    "name": "Kerem",
    "age": 22,
    "major": "CE"
}

for student_key, student_value in student_info.items():
    print(student_key, student_value)

# .items() şu tarz tuple'lar üretir:
#
# ("name", "Kerem")
# ("age", 22)
#
# key, value ile bunları unpack ediyoruz.


# ============================================================
# 9) ENUMERATE İLE UNPACKING
# ============================================================

print("\n----- Enumerate -----")

city_temperatures = [
    ("ankara", 23.5),
    ("kayseri", 22.0)
]

for city_index, (city_name, city_temp) in enumerate(city_temperatures):
    print(city_index, city_name, city_temp)

# enumerate bize index + item verir.


# ============================================================
# 10) LIST COMPREHENSION
# ============================================================

print("\n----- List Comprehension -----")

# Normal yöntem:

square_loop = []

for square_number in range(8):
    if square_number % 2 == 0:
        square_loop.append(square_number * square_number)

print(square_loop)


# Comprehension:

square_comprehension = [
    square_number * square_number
    for square_number in range(8)
    if square_number % 2 == 0
]

print(square_comprehension)

print(square_loop == square_comprehension)
# True


# Genel yapı:
#
# [expression for item in iterable if condition]


# ============================================================
# 11) COMPREHENSION'DA FILTER
# ============================================================

print("\n----- Comprehension Filter -----")

filter_temps = [18.5, 24.0, 31.2, 27.9]

hot_temps = [
    temp
    for temp in filter_temps
    if temp > 25
]

print(hot_temps)
# [31.2, 27.9]

# if sonda ise:
# bazı elemanları filtreler.


# ============================================================
# 12) COMPREHENSION'DA IF / ELSE
# ============================================================

print("\n----- Comprehension If Else -----")

label_temps = [18.5, 24.0, 31.2, 27.9]

temp_labels = [
    "hot" if temp > 25 else "ok"
    for temp in label_temps
]

print(temp_labels)

# ['ok', 'ok', 'hot', 'hot']

# Burada eleman sayısı değişmedi.
# Her eleman için bir değer seçtik.


# ============================================================
# 13) DICT COMPREHENSION
# ============================================================

print("\n----- Dict Comprehension -----")

temps_celsius = {
    "ankara": 23.5,
    "istanbul": 25.1,
    "kayseri": 22.0
}

temps_fahrenheit = {
    city: round(celsius * 9 / 5 + 32, 1)
    for city, celsius in temps_celsius.items()
}

print(temps_fahrenheit)

# Genel yapı:
#
# {
#     key: value
#     for item in iterable
# }


# ============================================================
# 14) SET COMPREHENSION
# ============================================================

print("\n----- Set Comprehension -----")

remainder_values = {
    number % 3
    for number in range(12)
}

print(remainder_values)

# {0, 1, 2}

# Set tekrar eden değerleri tutmaz.


# ============================================================
# 15) NESTED COMPREHENSION
# ============================================================

print("\n----- Nested Comprehension -----")

nested_matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

flat_matrix = [
    value
    for row in nested_matrix
    for value in row
]

print(flat_matrix)

# [1, 2, 3, 4, 5, 6]

# Aynı mantık:
#
# for row in nested_matrix:
#     for value in row:


# ============================================================
# 16) NESTED COMPREHENSION İLE TRANSPOSE
# ============================================================

print("\n----- Nested Comprehension Transpose -----")

transpose_matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed_matrix = [
    [row[column_index] for row in transpose_matrix]
    for column_index in range(len(transpose_matrix[0]))
]

print(transposed_matrix)

# [[1, 4], [2, 5], [3, 6]]


# ============================================================
# 17) ITERABLE VE ITERATOR
# ============================================================

print("\n----- Iterator -----")

iterator_values = [10, 20, 30]

number_iterator = iter(iterator_values)

print(next(number_iterator))
# 10

print(next(number_iterator))
# 20

print(next(number_iterator))
# 30


# Bir sonraki next() StopIteration verir.

try:
    print(next(number_iterator))

except StopIteration:
    print("Iterator bitti")


# ============================================================
# 18) ITERABLE İLE ITERATOR FARKI
# ============================================================

print("\n----- Iterable vs Iterator -----")

iterable_numbers = [1, 2, 3]

iterator_object = iter(iterable_numbers)

print(iter(iterable_numbers) is iterable_numbers)
# False

print(iter(iterator_object) is iterator_object)
# True


print(list(iterable_numbers))
print(list(iterable_numbers))

# Liste tekrar tekrar kullanılabilir.


print(list(iterator_object))
print(list(iterator_object))

# Iterator tüketilir.
# İkinci kullanımda boş kalır.


# ============================================================
# 19) GENERATOR FUNCTION
# ============================================================

print("\n----- Generator -----")

def countdown_generator(start_number):

    print("Generator başladı")

    while start_number > 0:

        yield start_number

        start_number -= 1

    print("Generator bitti")


countdown_values = countdown_generator(3)

print("Generator oluşturuldu")

# Fonksiyon henüz tam çalışmadı.
# yield değer istendiğinde çalışır.

for countdown_value in countdown_values:
    print(countdown_value)


# ============================================================
# 20) YIELD NEDİR?
# ============================================================

# return:
# fonksiyonu tamamen bitirir.

# yield:
# bir değer verir
# ve fonksiyonu o noktada DURAKLATIR.

# Sonraki next() çağrısında
# kaldığı yerden devam eder.


# ============================================================
# 21) SONSUZ GENERATOR
# ============================================================

print("\n----- Infinite Generator -----")

from itertools import islice

def fibonacci_generator():

    fib_a = 0
    fib_b = 1

    while True:

        yield fib_a

        fib_a, fib_b = fib_b, fib_a + fib_b


first_ten_fibonacci = list(
    islice(fibonacci_generator(), 10)
)

print(first_ten_fibonacci)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Generator sonsuz olabilir.
# islice ile sadece istediğimiz kadarını aldık.


# ============================================================
# 22) GENERATOR EXPRESSION
# ============================================================

print("\n----- Generator Expression -----")

generator_squares = (
    number * number
    for number in range(5)
)

print(generator_squares)

print(next(generator_squares))
# 0

print(next(generator_squares))
# 1


# List comprehension:
#
# [x*x for x in ...]
#
# hemen liste üretir.


# Generator expression:
#
# (x*x for x in ...)
#
# lazy çalışır.


# ============================================================
# 23) GENERATOR TEK KULLANIMLIKTIR
# ============================================================

print("\n----- Generator Single Use -----")

single_generator = (
    number * number
    for number in range(4)
)

print(sum(single_generator))
# 14

print(sum(single_generator))
# 0

print(list(single_generator))
# []

# Generator tüketildi.


# ============================================================
# 24) ITERTOOLS - CHAIN
# ============================================================

print("\n----- itertools.chain -----")

from itertools import chain

combined_stream = chain(
    [1, 2],
    (3, 4),
    range(5, 7)
)

print(list(combined_stream))

# [1, 2, 3, 4, 5, 6]


# ============================================================
# 25) ITERTOOLS - COUNT + ISLICE
# ============================================================

print("\n----- itertools.count -----")

from itertools import count

id_generator = count(start=100)

first_ids = list(
    islice(id_generator, 3)
)

print(first_ids)

# [100, 101, 102]


# ============================================================
# 26) DICT.GET İLE SAYMA
# ============================================================

print("\n----- dict.get -----")

count_word = "mississippi"

manual_counts = {}

for character in count_word:

    manual_counts[character] = (
        manual_counts.get(character, 0) + 1
    )

print(manual_counts)

# get(character, 0):
#
# key varsa değerini al
# key yoksa 0 kullan


# ============================================================
# 27) COUNTER
# ============================================================

print("\n----- Counter -----")

from collections import Counter

character_counter = Counter(count_word)

print(character_counter)

print(character_counter.most_common(2))

# En sık geçen 2 karakter


print(character_counter["s"])
# 4

print(character_counter["z"])
# 0

# Counter'da olmayan key için 0 döner.


# ============================================================
# 28) DEFAULTDICT
# ============================================================

print("\n----- defaultdict -----")

from collections import defaultdict

weather_readings = [
    ("ankara", 23),
    ("istanbul", 25),
    ("ankara", 24),
    ("kayseri", 21)
]

temperature_groups = defaultdict(list)

for reading_city, reading_temp in weather_readings:

    temperature_groups[reading_city].append(
        reading_temp
    )

print(dict(temperature_groups))


temperature_averages = {
    city: sum(values) / len(values)
    for city, values in temperature_groups.items()
}

print(temperature_averages)

# defaultdict(list):
#
# key ilk kez kullanıldığında
# otomatik olarak [] oluşturur.


# ============================================================
# 29) DEQUE
# ============================================================

print("\n----- deque -----")

from collections import deque

number_queue = deque([1, 2, 3])

number_queue.appendleft(0)
number_queue.append(4)

print(number_queue)

removed_number = number_queue.popleft()

print("Çıkan:", removed_number)
print("Kalan:", number_queue)

# deque:
# hem baştan hem sondan hızlı ekleme / silme sağlar.


# ============================================================
# 30) DEQUE MAXLEN
# ============================================================

print("\n----- deque maxlen -----")

last_three = deque(maxlen=3)

for newest_number in range(6):

    last_three.append(newest_number)

print(last_three)

# deque([3, 4, 5], maxlen=3)

# Yeni eleman geldiğinde
# en eski eleman otomatik silinir.


# ============================================================
# 31) DOSYA YAZMA VE OKUMA
# ============================================================

print("\n----- File -----")

from pathlib import Path

sample_file_path = Path("lecture3_sample.txt")

sample_file_path.write_text(
    "Python\nScientific Programming\n",
    encoding="utf-8"
)

with open(
    sample_file_path,
    "r",
    encoding="utf-8"
) as sample_file:

    for sample_line in sample_file:

        print(sample_line.rstrip())


print("Dosya kapalı mı?", sample_file.closed)

# with bloğu bittiğinde
# dosya otomatik kapanır.


# ============================================================
# 32) CSV DOSYASI
# ============================================================

print("\n----- CSV -----")

import csv

csv_file_path = Path("lecture3_sensor.csv")

csv_file_path.write_text(
    "time,temperature,humidity\n"
    "0,22.1,40\n"
    "1,22.5,41\n"
    "2,23.0,43\n",
    encoding="utf-8"
)


with open(
    csv_file_path,
    newline="",
    encoding="utf-8"
) as csv_file:

    csv_rows = list(
        csv.DictReader(csv_file)
    )


print(csv_rows)

print(csv_rows[0])

# Önemli:
# CSV'den gelen değerler STRING olur.

print(type(csv_rows[0]["temperature"]))
# str


temperature_float = float(
    csv_rows[0]["temperature"]
)

print(type(temperature_float))
# float


# ============================================================
# 33) CSV'DE split(",") NEDEN RİSKLİ?
# ============================================================

print("\n----- CSV Quoted Value -----")

quoted_csv_line = 'kayseri,"Kayseri, TR",22.0'

print(quoted_csv_line.split(","))

# Yanlış parçalar.


correct_csv_values = next(
    csv.reader([quoted_csv_line])
)

print(correct_csv_values)

# csv.reader quote işaretlerini doğru yorumlar.


# ============================================================
# 34) KENDİ CONTEXT MANAGER'IMIZ
# ============================================================

print("\n----- Context Manager -----")

import time

from contextlib import contextmanager


@contextmanager
def timed_block(label):

    start_time = time.perf_counter()

    try:

        yield

    finally:

        elapsed_ms = (
            time.perf_counter() - start_time
        ) * 1000

        print(
            f"[{label}] {elapsed_ms:.2f} ms"
        )


with timed_block("Toplama"):

    timed_total = sum(
        number * number
        for number in range(10_000)
    )


print(timed_total)

# yield öncesi:
# with bloğu başlamadan önce

# yield:
# with bloğunun çalıştığı yer

# finally:
# with bloğu bitince


# ============================================================
# 35) DECORATOR NEDİR?
# ============================================================

# Yukarıdaki:

# @contextmanager

# bir decorator'dır.

# Decorator:
# bir fonksiyonu alır
# ve ona yeni davranış ekleyen / onu saran
# başka bir yapı üretir.


# ============================================================
# 36) TRY / EXCEPT / ELSE / FINALLY
# ============================================================

print("\n----- try except else finally -----")

def convert_to_float(text_value):

    try:

        converted_value = float(text_value)

    except ValueError:

        print("except çalıştı")

        return None

    else:

        print("else çalıştı")

        return converted_value

    finally:

        print("finally her zaman çalıştı")


print(convert_to_float("2.5"))

print(convert_to_float("abc"))


# try:
# önce çalışır

# except:
# hata varsa çalışır

# else:
# hata yoksa çalışır

# finally:
# her durumda çalışır


# ============================================================
# 37) CUSTOM EXCEPTION
# ============================================================

print("\n----- Custom Exception -----")


class DataFormatError(ValueError):
    """Veri formatı hatalı olduğunda kullanılır."""


def parse_sensor_line(sensor_line):

    try:

        time_text, temperature_text, humidity_text = (
            sensor_line.split(",")
        )

        return (
            int(time_text),
            float(temperature_text)
        )

    except ValueError as original_error:

        raise DataFormatError(
            f"Hatalı satır: {sensor_line!r}"
        ) from original_error


print(
    parse_sensor_line("0,22.1,40")
)


try:

    parse_sensor_line("2,oops,41")

except DataFormatError as data_error:

    print("Yakalandı:", data_error)

    print(
        "Asıl sebep:",
        repr(data_error.__cause__)
    )


# ============================================================
# 38) raise ... from
# ============================================================

# Şu yapı:

# raise DataFormatError(...) from original_error

# yeni hatanın altında
# orijinal hatayı saklar.

# Böylece:
#
# DataFormatError
# neden oluştu?
#
# -> ValueError


# ============================================================
# 39) HATALARI SESSİZCE YUTMA
# ============================================================

# KÖTÜ:

# try:
#     ...
# except Exception:
#     pass


# Çünkü bütün hataları gizler.


# DAHA DOĞRU:

# try:
#     ...
# except ValueError:
#     print("Beklenen veri hatası oluştu")


# Sadece beklediğin hata tipini yakala.


# ============================================================
# 40) DATACLASS
# ============================================================

print("\n----- dataclass -----")

from dataclasses import dataclass


@dataclass
class SensorReading:

    time_s: int

    temperature_c: float

    humidity: float = 0.0


sensor_one = SensorReading(
    0,
    22.1,
    40
)

sensor_two = SensorReading(
    0,
    22.1,
    40
)


print(sensor_one)

print(sensor_one == sensor_two)
# True

print(sensor_one.temperature_c)
# 22.1


# dataclass otomatik olarak:
#
# __init__
# __repr__
# __eq__
#
# gibi şeyleri üretir.


# ============================================================
# 41) FROZEN DATACLASS
# ============================================================

print("\n----- Frozen Dataclass -----")


@dataclass(frozen=True)
class CoordinatePoint:

    x: float

    y: float


fixed_point = CoordinatePoint(
    1.0,
    2.0
)


print(fixed_point)


try:

    fixed_point.x = 5.0

except AttributeError as frozen_error:

    print(
        type(frozen_error).__name__
    )


# frozen=True:
# dataclass immutable olur.


point_dictionary = {
    fixed_point: "start"
}

print(point_dictionary)

# Hashable olduğu için dict key olabilir.


# ============================================================
# 42) GENERATOR PIPELINE
# ============================================================

print("\n----- Generator Pipeline -----")


pipeline_path = Path(
    "lecture3_pipeline.csv"
)

pipeline_path.write_text(
    "time,temperature,humidity\n"
    "0,22.1,40\n"
    "1,22.5,41\n"
    "2,oops,41\n"
    "3,22.9,43\n"
    "4,23.4,44\n"
    "5,,45\n"
    "6,24.0,47\n",
    encoding="utf-8"
)


@dataclass
class PipelineReading:

    time_s: int

    temperature_c: float

    humidity: float


# ------------------------------------------------------------
# STAGE 1
# CSV SATIRLARINI TEK TEK ÜRET
# ------------------------------------------------------------

def read_sensor_rows(path):

    with open(
        path,
        newline="",
        encoding="utf-8"
    ) as pipeline_file:

        yield from csv.DictReader(
            pipeline_file
        )


# ============================================================
# 43) yield from
# ============================================================

# yield from iterable

# yaklaşık olarak:

# for item in iterable:
#     yield item

# demektir.


# ------------------------------------------------------------
# STAGE 2
# STRING VERİLERİ DÖNÜŞTÜR
# ------------------------------------------------------------

def parse_sensor_rows(
    rows,
    problems
):

    for sensor_row in rows:

        try:

            yield PipelineReading(
                int(sensor_row["time"]),
                float(sensor_row["temperature"]),
                float(sensor_row["humidity"])
            )

        except ValueError:

            problems["bad row"] += 1


# ------------------------------------------------------------
# STAGE 3
# SICAK OLANLARI SEÇ
# ------------------------------------------------------------

def select_hot_readings(
    readings,
    threshold
):

    for sensor_reading in readings:

        if (
            sensor_reading.temperature_c
            >= threshold
        ):

            yield sensor_reading


# ============================================================
# 44) PIPELINE'I ÇALIŞTIR
# ============================================================

pipeline_problems = Counter()

hot_readings = list(

    select_hot_readings(

        parse_sensor_rows(

            read_sensor_rows(
                pipeline_path
            ),

            pipeline_problems
        ),

        threshold=22.6
    )
)


for hot_reading in hot_readings:

    print(hot_reading)


print(
    "Hatalar:",
    dict(pipeline_problems)
)


hot_mean = (
    sum(
        reading.temperature_c
        for reading in hot_readings
    )
    / len(hot_readings)
)


print(
    "Ortalama:",
    round(hot_mean, 2)
)


# Önemli:
#
# Generator'lar lazy olduğu için
# list(...) çağrılana kadar
# pipeline gerçekten tüketilmez.


# ============================================================
# 45) HEAPQ - TOP K
# ============================================================

print("\n----- heapq -----")

import heapq

heap_temperatures = [
    22.1,
    25.3,
    19.8,
    27.4,
    23.0,
    26.1
]

largest_three = heapq.nlargest(
    3,
    heap_temperatures
)

print(largest_three)

# [27.4, 26.1, 25.3]

# Tüm listeyi sıralamadan
# en büyük k elemanı bulmak için kullanılabilir.


# ============================================================
# 46) BISECT
# ============================================================

print("\n----- bisect -----")

from bisect import bisect_left, insort

sorted_grades = [
    50,
    60,
    70,
    80,
    90
]

insert_index = bisect_left(
    sorted_grades,
    75
)

print(insert_index)
# 3


insort(
    sorted_grades,
    75
)

print(sorted_grades)

# [50, 60, 70, 75, 80, 90]

# bisect sıralı listelerde kullanılır.


# ============================================================
# 47) itertools.groupby
# ============================================================

print("\n----- groupby -----")

from itertools import groupby

group_pairs = [
    ("B", 5),
    ("A", 1),
    ("B", 7),
    ("A", 2)
]


# groupby sadece YAN YANA olan
# aynı key değerlerini gruplar.


sorted_pairs = sorted(group_pairs)


for group_key, group_values in groupby(
    sorted_pairs,
    key=lambda pair: pair[0]
):

    print(
        group_key,
        [value for _, value in group_values]
    )


# Bu yüzden çoğu durumda
# groupby'dan önce sıralama gerekir.


# ============================================================
# 48) ENUM
# ============================================================

print("\n----- Enum -----")

from enum import Enum


class TemperatureStatus(Enum):

    OK = "ok"

    WARN = "warn"

    FAIL = "fail"


def status_for_temperature(temp_value):

    if temp_value >= 30:

        return TemperatureStatus.FAIL

    if temp_value >= 25:

        return TemperatureStatus.WARN

    return TemperatureStatus.OK


status_result = status_for_temperature(
    26.0
)

print(status_result)

print(
    status_result
    is TemperatureStatus.WARN
)

# Enum:
# sabit ve isimlendirilmiş değer kümesi oluşturur.


# ============================================================
# 49) LECTURE 3 EN ÖNEMLİ ÖZET
# ============================================================

# SLICING
# liste parçası almak
#
# x[start:stop:step]


# UNPACKING
#
# a, b = ...
# first, *rest = ...


# COMPREHENSION
#
# [expression for x in values if condition]


# GENERATOR
#
# yield
#
# lazy çalışır
# tek kullanımlıktır


# Counter
# -> sayma


# defaultdict
# -> gruplama


# deque
# -> queue / rolling window


# with
# -> resource otomatik kapanır


# csv
# -> CSV'yi güvenli parse eder


# try / except / else / finally
# -> hata yönetimi


# custom exception
# -> anlamlı özel hata tipi


# dataclass
# -> veri kayıtları


# generator pipeline
# -> veriyi tek tek işler


# ============================================================
# 50) NOTEBOOK'TAKİ GERÇEK EXERCISES
# CEVAPLARINI ŞİMDİLİK YAZMIYORUZ
# ============================================================


# EXERCISE 1
#
# char_freq_loop(text) fonksiyonu yaz.
#
# dict.get kullanarak karakterlerin
# kaç kez geçtiğini bul.
#
# Daha sonra aynı işi:
#
# char_freq_counter(text)
#
# fonksiyonunda Counter ile yap.
#
# İki sonucu karşılaştır.


# ------------------------------------------------------------


# EXERCISE 2
#
# top_k(values, k)
#
# fonksiyonunu yaz.
#
# heapq.nlargest kullan.
#
# Sonucunu:
#
# sorted(values, reverse=True)[:k]
#
# ile karşılaştır.


# ------------------------------------------------------------


# EXERCISE 3
#
# Generator pipeline'a:
#
# select_humid(
#     readings,
#     min_humidity
# )
#
# adında yeni bir stage ekle.
#
# humidity değeri belirtilen minimumdan
# büyük veya eşit olanları yield et.


# ------------------------------------------------------------


# EXERCISE 4
#
# rolling_mean(iterable, k)
#
# generator fonksiyonunu yaz.
#
# deque(maxlen=k) kullan.
#
# Son k değerin ortalamasını
# pencere dolduktan sonra yield et.
#
# Örnek:
#
# rolling_mean(
#     [1, 2, 3, 4, 5],
#     3
# )
#
# sonucu:
#
# [2.0, 3.0, 4.0]


# ------------------------------------------------------------


# EXERCISE 5
#
# OutOfRangeError(ValueError)
#
# adında custom exception oluştur.
#
# Sıcaklık:
#
# -50 ile 60
#
# aralığının dışındaysa
# bu hatayı raise et.
#
# parse pipeline'ında bu satırları
# diğer hatalardan ayrı say.