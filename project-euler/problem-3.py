def is_prime(num):
    """
    Check if the given number is a prime
    """

    if num<2:
        return False
    
    i = 2
    terminator = num**0.5

    while i<=terminator:
        if num%i == 0:
            return False
        i=i+1

    return True


value = 600851475143

terminator = value**0.5
prime_fac = None
i = 1

while i<=terminator:
    if value%i == 0:
        if is_prime(i):
            prime_fac = i
        if is_prime(value//i):
            prime_fac = value//i
            break
    i=i+1 

print(prime_fac)


#Time Complexity O(n^0.5) (n=value)
#Space Complexity O(1)