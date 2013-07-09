a = 0
b = 1
res = 0

while a <= 4000000:
    if (a % 2 == 0):
        res = res + a
    a, b = b, a+ b
print res