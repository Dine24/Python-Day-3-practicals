def addBinary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    return bin(c)[2:]

a = "11"
b = "1"
print(addBinary(a, b))
