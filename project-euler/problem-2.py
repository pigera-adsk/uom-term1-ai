a = 0
b = 1
total = 0
terminator = 100

while a<=terminator:
    a,b = a+b,a
    if a%2 == 0:
        total = total + a

print(total)


#Time Complexity O(log(n)) (n=terminator)
#Space Complexity O(1)