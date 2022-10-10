nilai = [32,54,65,24,75,23,67,34]
print(nilai)
# hitung banyak elemen
print(len(nilai))

set_ex = set([32,54,65,24,75,23,67,34])
print(type(set_ex))
print(set_ex)
print(len(set_ex))

# len() juga dapat menghitung jumlah karakter str
print(len("Halo, saya Fariz Fadila"))

# return min or max value
nilai = [32,54,65,24,75,23,67,34]
print("nilai min:",min(nilai))
print("nilai max:",max(nilai))

# menghitung value dengan count()
nilai = [32,54,32,24,75,32,67,34]
print(nilai.count(32))
string = "saya sedang belajar python"
print(string.count("a"))

'''
JOIN AND REPLICATE LIST
'''
nilai = [32,54,65,24,75,23,67,34]
string = ["F","A","R","I","Z"]
join_list = nilai + string
print(join_list)

print(string*2)

# RANGE
# range(awal, akhir, step)
for i in range(2,20,2):
    print(i)

print([i for i in range(2,20,2)])

# IN, NOT IN
# return boolean
print("makan" in "Fariz Fadila sedang makan") # True
print("kambing" not in "Fariz sedang makan") #False

# INPUT MULTIPLE VAR FROM LIST OR TUPLE
list = ["Fariz", 175, 60]
nama, tb, bb = list
print(nama)
print(tb)
print(bb)

tuple = tuple(["Fariz", 175, 60])
nama, tb, bb = tuple
print(type(tuple))
print(nama)
print(tb)
print(bb)

# list hanya punya 3 elemen
# nama, tb, bb, pendidikan = list # error

# SORT LIST
nilai = [32,54,65,24,75,23,67,34]
nilai.sort()
print(nilai)
# sort descending
nilai = [32,54,65,24,75,23,67,34]
nilai.sort(reverse=True)
print(nilai)