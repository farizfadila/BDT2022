import modul_oop_16 as md

print(md.Kalkulator.i)

'''
Object: an instance of a class
'''
objek_calc = md.Kalkulator()
print(objek_calc.i)
print(objek_calc.f())
# panggil nilai x di __init__
print(objek_calc.x)

# TEST GANTI VALUE x DI __init__
objek_calc.x = "nilai x pada objek_calc"
md.Kalkulator.__init__.x = "nilai x pada __init__ modul terganti"
print("nilai x pada objek_calc setelah diganti: ",objek_calc.x) # nilai x di __init__ tidak berubah

# TEST GANTI VALUE i DI class Kalkulator
objek_calc.i = "nilai i pada objek_calc di class modul terganti"
md.Kalkulator.i = "nilai i di class modul terganti"
print("Nilai i pada objek_calc: ", objek_calc.i)

calc2 = md.Kalkulator()
print("Nilai x di __init__ pada calc2: ",calc2.x)
print("Nilai i di class pada calc2: ",calc2.i)

