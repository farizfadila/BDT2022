def printinfo(*args, **kwargs):
    for x in args:
        print("Argumen posisi {}".format(x))
    for key, value in kwargs.items():
        print("Argumen kata kunci {}:{}".format(key,value))
print("*"*10)
printinfo()
printinfo(524,24,324)
print("*"*10)
printinfo(p=42,q=42,r=4)
print("*"*10)
printinfo(43,65,r=53,s=56)
print("*"*10)
#printinfo(r=53,s=56,43,65) #positional argument harus didahulukan
print("*"*10)
printinfo(*(43,65),**{"d":64,"w":23})
print("*"*10)

# Lambda Function
kali_lambda = lambda nilai1, nilai2: nilai1 * nilai2
print("Hasil:",kali_lambda(11,21))