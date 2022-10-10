'''
Ada banyak tipe data dalam python.
- Numbers (int, float, complex)
- String
- Boolean
'''

# TIPE DATA NUMBERS

x = 424
print(x, "bertipe", type(x))

y = 24.4242
print(y, "bertipe", type(y))

z = 235 + 43j
print(z, "bertipe", type(z))

# panjang int tidak terbatas,
# tapi terbatas oleh memori yang tersedia

x = [0]*10005;  # membuat 10000 array
x[1] = 1;

for i in range(2,10001):
    x[i] = x[i-1] + x[i-2]
print(x[10000])

# tipe data float dibatasi 15 desimal
b=2**(1/2)
print(b)

# TIPE DATA STRING

a = "Lorem ipsum dolor sit amet."
print(a)

b = '''
ini adalah string
'''
print(b)

# TIPE DATA BOOLEAN

a = True
print(a, "bertipe", type(a))

a = False
print(a, "bertipe", type(a))