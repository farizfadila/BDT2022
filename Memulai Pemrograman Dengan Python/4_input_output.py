print("Halo, nama saya {} {}".format("fariz","fadila")) # output yang dihasilkan "hai fariz"

'''
INPUT VARIABEL PADA STRING
‘%d’ for integers
‘%f’ for floating-point numbers
‘%b’ for binary numbers
‘%o’ for octal numbers
‘%x’ for octal hexadecimal numbers
‘%s’ for string
‘%e’ for floating-point in an exponent format

'''
nama = "Fariz Fadila"
print("Halo, saya %s" % nama)


nama = "Fariz"
umur = 17.67
print("Namaku %s, umurku %3.5f" %(nama, umur))

list_angka = [1,2,3,4,5,6,7,8,9]
print("ini adalah list: %s" % list_angka)

'''
FUNGSI INPUT()
'''
item1 = int(input("Masukkan harga item 1:"))
item2 = int(input("Masukkan harga item 2:"))
jumlah = item1 + item2
print("Anda harus bayar ", jumlah)

# print tidak bisa menampilkan int
# print hanya menampilkan str
# eva() jadi solusi menampilkan kalkulasi string pada print
print(eval("523453*42"))