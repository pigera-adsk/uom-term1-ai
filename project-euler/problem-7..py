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


check = 1
count = 0
expected = 100000

while count<expected :
    check = check + 1
    if is_prime(check):
        count = count + 1
    
print(check)


#Time Complexity O((n.ln(n)^1.5) (n=expected)
#Space Complexity O(1)