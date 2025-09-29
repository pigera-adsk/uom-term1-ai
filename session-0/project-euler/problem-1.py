#Sum of multiplies of 3 or 5 below 1000

total = 0
terminator = 1000

for i in range(terminator):
    if i%3 == 0 or i%5 == 0:
        total = total + i

print(total)


#Time Complexity O(n) (n=terminator)
#Space Complexity O(1)