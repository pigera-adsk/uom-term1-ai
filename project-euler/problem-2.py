#Sum of even Fibonacci numbers below 4,000,000

a = 0
b = 1
total = 0
terminator = 4000000

while a<=terminator:
    a,b = a+b,a #Generate Fibonacci sequence
    if a%2 == 0:
        total = total + a

print(total)


#Time Complexity O(log(n)) (n=terminator)
#Space Complexity O(1)