def cetak(teks):
    print(teks)
    return

cetak("Fariz Fadila")
cetak("Ini dicetak dari fungsi")

'''
RETURN
- exit from function
'''
def perkalian(num1,num2):
    hasil = num1 * num2
    print("Dicetak dari dalam function: {}".format(hasil))

test1 = perkalian(5,5)
print("Hasil tanpa return {}".format(test1)) # Hasil None karena tidak di return

def perkalian(num1,num2):
    hasil = num1 * num2
    print("Dicetak dari dalam function: {}".format(hasil))
    return hasil # akan menyimpan var hasil setelah function dijalankan

test2 = perkalian(5,5)
print("Hasil dengan return {}".format(test2)) # Hasil 25 karena di return

def kuadrat(num):
    return num**2
a = 10
a_kuadrat = kuadrat(a)
print(a_kuadrat)

def ubah(my_list):
    my_list.append([1,2,3])
    print("Nilai di dalam function: {}".format(my_list))

test = [24,54,65]
ubah(test)
print("Nilai diluar fungsi: {}".format(test))

def ganti(my_list):
    my_list = [1,2,3,4]
    print("Nilai dalam function: {}".format(my_list))

test_list = [45,45,45]
ganti(test_list)
print("Nilai diluar function {}".format(test_list))