# Mutable = Değiştirilebilir 
# Python'daki bir nesnenin oluşturulduktan sonra aynı nesne 
#olarak değiştirilebilir olup olmadığınını anlatıyor
# list
# dict
# set
print("-----Mutable------ ")

a = [1,2,3,4]  # Liste

print(id(a))
#140571798559488

a.append(4)

print(a)

print(id(a))
# 139837992491776






# # immutable 
# int
# float
# str
# tuple
# frozenset
# bunlar immutable tipler
print("-----Imutable------ ")
m = 10 
print(id(m))

m+=1
print(id(m))

# 139809305578704
# 139809305578736


x = 100
y = x

print(id(x), id(y), x is y)

y = y + 1 # yeni bir int değeri atıldı yani yeri değişti  100 iken --> 101 oldu

print(id(x), id(y), x is y)

print("Aliasing")
a = [1, 2, 3]

b = a

b.append(5)

print(a)


print("-----Copy------ ")


import copy

k = [1,2,3]
l = k
m = k.copy()
n = copy.deepcopy(k)

k.append(4)

print("k:", k)
print("l (alias):", l)
print("m (shallow):", m)
print("n (deep):", n)

# k: [1, 2, 3, 4]
# l (alias): [1, 2, 3, 4]
# m (shallow): [1, 2, 3]
# n (deep): [1, 2, 3]


print("----- Shallow Copy Nested List ------")

p = [[1, 2], [3, 4]]

q = p.copy()

q[0].append(99)

print("p:", p)
print("q:", q)

# p: [[1, 2, 99], [3, 4]]
# q: [[1, 2, 99], [3, 4]]

print("----- Shallow Copy ID Kontrol ------")

r = [[10, 20], [30, 40]]

s = r.copy()

print("Dış liste:")
print(id(r))
print(id(s))

print("İç liste:")
print(id(r[0]))
print(id(s[0]))

print("----- Deep Copy ------")

u = [[1, 2], [3, 4]]

v = copy.deepcopy(u)

v[0].append(42)

print("u:", u)
print("v:", v)


print("----- Deep Copy ID Kontrol ------")

w = [[5, 6], [7, 8]]

z = copy.deepcopy(w)

print("Dış liste:")
print(id(w))
print(id(z))

print("İç liste:")
print(id(w[0]))
print(id(z[0]))


list_one = list_two = [1, 2, 3]

list_two.append(5)

print(list_one)
# [1, 2, 3, 5]



num_one, num_two = 1, 2

print(num_one, num_two)
# 1 2

num_one, num_two = num_two, num_one

print(num_one, num_two)
# 2 1