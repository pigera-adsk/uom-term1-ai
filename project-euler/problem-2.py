a = 0
b = 1
total = 0

while a<=4000000:
    a,b = a+b,a
    if a%2 == 0:
        total = total + a

print(total)