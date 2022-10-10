nilai = int(input("Masukkan nilai Anda"))
if nilai>=70:
    print("Anda lulus")
else:
    print("Anda tidak lulus")

# Ganjil Genap
bilangan = 97
if bilangan % 2 == 0:
    print("Bilangan {} adalah bilangan genap".format(bilangan))
else:
    print("Bilangan {} adalah bilangan ganjil.".format(bilangan))

# Program nilai
nilai = int(input("Masukkan nilai tugas Anda: "))
if nilai>80:
    print("Selamat! Anda mendapat nilai A")
elif nilai>70:
    print("Selamat! Anda mendapat nilai B")
elif nilai>60:
    print("Selamat! Anda mendapat nilai C")
else:
    print("Nilai Anda D")

# Check positive, negative, zero number
bilangan = -3
if bilangan > 0:
    print("Bilangan {} adalah bilangan positif.".format(bilangan))
elif bilangan < 0:
    print("Bilangan {} adalah bilangan negatif.".format(bilangan))
else:
    "Bilangan tersebut adalah bilangan nol."

nilai = 87
print("Selamat" if nilai > 70 else "Belajar lagi")

lulus = True
print(("perbaiki","selamat")[lulus])