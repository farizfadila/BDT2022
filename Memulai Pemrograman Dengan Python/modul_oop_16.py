class Kalkulator:
    '''
    Ini adalah class Kalkulator sederhana
    '''
    i = "nilai i di class modul"

    '''
    Class's constructor
    biasanya kita perlu set nilai awal dari objek, namun dari sisi luar modul nilai tersebut tidak boleh dirubah, akan berbahaya jika di set di skala class, karena user dapat melakukan perubahan. Solusi: gunakan class's constructor untuk set nilai awal
    '''
    def __init__(self):
        self.x = "nilai x di __init__ modul" # nilai ini tidak dapat diakses dari luar modul

    def f(self):
        return "Hello World!"