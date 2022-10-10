# FOR
for i in "Fariz Fadila":
    print("Nama: {}".format(i))

nama = ["Doni","Slamet","Riko","Bunga"] 
for i in nama:
    print("Nama: {}".format(i))
for i in range(len(nama)):
    print("Nama: {}".format(nama[i]))

#WHILE
hitung = 0
while hitung < 10:
    print("Hitung: {}".format(hitung))
    hitung += 1

# while loop bersifat infinite loop saat kondisi selalu terpenuhi
angka = 0
while angka == True: # jika angka == False akan infinite loop
    x = int(input("Masukkan bilangan: "))
    print(x)

# Loop bertingkat
for i in range(0, 6):
    for j in range(0, 6 - i):
        print("*", end="")
    print("")