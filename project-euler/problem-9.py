expected_sum = 1000

#initiation
a = 1
b = a+1

while a<=expected_sum:
    c = (a**2 + b**2)**0.5
    if a+b+c == 1000:
        print(int(a*b*c))
        break
    elif a+b+c > 1000:
        a=a+1
        b = a+1
    b = b+1


#Time Complexity O(n^2) (n=expected_sum)
#Space Complexity O(1)