first_name = "fariz"
first_name = first_name.upper()
print(first_name)

last_name = "FADILA"
last_name = last_name.lower()
print(last_name)

# TRIM SPACE
# ada 3 jenis: rstrip(), lstrip(), strip()
print(len("Fariz       ".rstrip()))
print(len("      Fariz".lstrip()))
print(len("      Fariz   ".strip()))
print("*****Far*iz****Fadila***".strip("*"))

# CHECK AWALAN/AKHIRAN STR
# startswith(), endswith()
print("Fariz Fadila".startswith("Fa"))
print("Fariz Fadila".endswith("ila"))

# JOIN STRING
print("@".join(["Ini","Adalah","Python","Join"]))

# SPLIT (kebalikan JOIN)
print("Ini@Adalah@Python@Join".split("@"))

print('''Hai,
ini adalah contoh paragraf
yang ditulis dalam
bahasa python''')

print('''Hai,
ini adalah contoh paragraf
yang ditulis dalam
bahasa python'''.split("\n"))

# REPLACE
teks = "Kambing adalah hewan berkaki empat. Makanan Kambing adalah rumput. Fariz punya kambing. Kambingnya sulit gemuk."
print(teks.replace("Kambing","Sapi"))

# STRING CHECK
print("FARIZ FADILA".isupper())
print("fariz fadila".islower())

# CHAIN OF METHOD
print("FARIZ".lower().lower().upper())

# Return True when all are alphabet string
print("Fariz Fadila".isalpha())     #False
print("FarizFadila".isalpha())      #True

# Return True when all are alphabet and numeric
print("Fariz12345".isalnum())

#Return True when integer
print("52525.646".isdecimal())
print("52525".isdecimal())

# Return True when whitespace
print("         ".isspace())

# Return True when capital letters each first word
print("Ini Adalah Contoh Title".istitle())

# Buat input nama yang harus huruf kapital tiap awal kata dan tanpa karakter selain alphabet.
first_name = input("Masukkan nama depan Anda:")
last_name = input("Masukkan nama belakang Anda:")
while (first_name.isalpha() and last_name.isalpha()) and (first_name+" "+last_name).istitle():
    print("Halo, ",first_name,last_name)
    break
else:
    print("Masukkan nama dengan benar.")

# FORMATTING STRING
# zfill() untuk menambahkan 0 sebelah kiri
print("-0.45".zfill(7)) # -0.45 terhitung 5 karakter, output ditambah 2 karakter jadi -000.45
print("fariz".zfill(7))

'''
TEXT ALIGNMENT
- rjust(), ljust(), center()
- add whitespace to string
- defaultnya menambahkan spasi
'''
print("fariz".ljust(15,"-"))
print("fariz".rjust(15,"-"))
print("fariz".center(15,"-"))

'''
STRING LITERALS
- add ' to string
Solusi:
1. gunain "
2. gunain escape character "\"
'''
# print('Jum'at') #Error
print("Jum'at")
print('Jum\'at')

# RAW STRING
# escape character tidak dieksekusi
print(r"Jum'at \t \n")