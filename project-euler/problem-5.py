#Smallest number divisible by numbers from 1 to 20

from math import gcd

num = 1
end = 20

for i in range(end,0,-1):
    if num%i != 0 :
        num = num*i//gcd(num,i)   #make 'num' divisible by 'i' using smallest multiplier

print(num)


#Time Complexity O(nlog(n)) (n=end)
#Space Complexity O(1)