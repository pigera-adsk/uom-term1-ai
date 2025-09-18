from math import gcd

num = 1
end = 20

for i in range(end,0,-1):
    if num%i != 0 :
        num = num*i//gcd(num,i)    

print(num)