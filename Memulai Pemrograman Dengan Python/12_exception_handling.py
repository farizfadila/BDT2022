'''
Pada dasarnya python sudah menampilkan
error tertentu saat terjadi exception.
Namun error tersebut dapat ditampilkan
kembali dengan tru dan except
'''
num = 0
try:
    x = 1 / num
    print(x)
except ZeroDivisionError:
    print("Angka pembagi tidak boleh nol.")

# Handling file not exist
try:
    with open("sebuah_file_python.py") as file:
        print(file.read())
except (FileNotFoundError, ):
    print("File tidak ditemukan")

a = {"average": "15.0"}
try:
    print("Rata-rata {}".format(a["avg"]))
except KeyError:
    print("Kunci tidak ditemukan di dictionary.")
except ValueError:
    print("Nilai tidak sesuai")

try:
    print("Rata-rata {}".format(a["average"]/3))
except KeyError:
    print("Kunci tidak ditemukan di dictionary.")
except (ValueError, TypeError):
    print("Nilai atau tipe tidak sesuai.")

try:
    print("Pembulatan rata-rata: {}".format(int(a["average"])))
except (ValueError, TypeError) as err:
    print("Penanganan kesalahan: {}".format(err))

dict1 = {"rata-rata":"14.9"}
if "total" not in dict1:
    raise KeyError("dict harus memiliki total")