'''
LIST

- kumpulan array
- data type tidak selalu sama
- bisa diakses dengan indeks
'''

x = [1, 234.53, "ini string"]
print(x, "bertipe", type(x))
print(x[2])
print(x[-2])

# Menambah/merubah/menghapus elemen pada list
x[1] = 5464.46
print(x)

x.append(5)
print(x)

del x[0]
print(x)

# SLICING DENGAN STEP
a = list(range(0,11))
print(a)
print(a[1:11:2]) # output bil ganjil

# SLICING PADA STRING
a = "lorem ipsum dolor sit amet"
print(a[1])
print(a[0:5])
# a[1] = "test" # substr tidak bisa dirubah

'''
TUPLE
- hampir sama seperti list
- bisa di slicing
- tidak bisa dirubah
'''
t = (2, "ini tidak bisa dirubah", 24.43)
print(t[1])
# t[1] = "test merubah tuple"

'''
SET (HIMPUNAN)
- tidak dapat di slicing
'''
s = {1,2,3,4,5}
print(s)
# s[1]

'''
DICTIONARY
- seperti list
- dapat di slicing dengan key
'''
d = {1:"ini adalah value","kunci":2}
print(d[1])
print(d["kunci"])

'''
KONVERSI
'''
print(float(5))
print(int(5.6)) # akan dibulatkan kebawah
print(float("52352.53"), "bertipe", type(float("52352.53")))

print(list("hello"))
print(set("hello"))
print(tuple("hello"))
print(dict([[5,"value key 5"],["key kedua",64]]))