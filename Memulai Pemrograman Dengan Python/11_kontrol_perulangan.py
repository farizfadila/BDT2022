'''
BREAK
- atasi infinite loop dengan break sesuai dengan tingkatan kondisi looping
'''
for i in range(0,10,2):
    if i > 5:
        break
    print(i)

# CETAK BINTANG
for i in range(0,4):
    for j in range(0,4):
        if j<=i:
            print("*", end="")
        else:
            print("")
            break

'''
CONTINUE
- akan skip ke kondisi berikutnya.

Buat seperti berikut
*
**
***
****
*****
******
*******
********
*********
**********
'''
print("\n","-"*10)

jumlah_baris = 10
baris = 0
bintang = 0
while baris < jumlah_baris:
    if bintang == (baris+1):
        print("")
        bintang=0
        baris += 1
        continue
    print("*",end="")
    bintang += 1

print("-"*10)

for n in range(2, 21):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n/x)
            break
    else:
        print(n, "adalah bilangan prima")
    
# Else after while
num = 10
while num >= 4:
    print(num)
    if num == 6:
        break    
    num -= 1
else:
    print("Looping selesai")
# "Looping selesai" tidak dieksekusi karena kondisi break telah terpenuhi terlebih dahulu

# PASS
angka = ""
while (angka != "exit"):
    angka = input("Masukkan bilangan bulat:")
    print(int(angka))
    break
# Statement diatas akan error jika input selain number (termasuk jika input "exit").
# solusi: gunakan pass untuk handling error
import sys
data=''
while(data!='exit'):
    try:
        data=input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))

# LIST COMPREHENSION
num_list = [1, 2, 3, 4, 5]
pangkat = []
for i in num_list:
    pangkat.append(i**2)
print(pangkat)

pangkat = [i**2 for i in num_list]
print(pangkat)

# Find duplicate element
list1 = ["f","a","r","i","z"]
list2 = ["f","a","d","i","l","a"]
duplikat = []
for x in list1:
    for y in list2:
        if x==y:
            duplikat.append(x)
print(duplikat)

duplikat = [x for x in list1 for y in list2 if x==y]
print(duplikat)

# change every element in list to lower case
list1 = ["Fariz","Fadila","Sedang","Makan"]
lower_case = [x.lower() for x in list1]
print(lower_case)