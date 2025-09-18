def is_prime(num):
    """
    Check if the given integer(>2) is a prime
    """

    i = 2
    terminator = num**0.5

    while i<=terminator:
        if num%i == 0:
            return False
        i=i+1

    return True

end = 1000000
total = 2

for i in range(3,end,2):
    if is_prime(i):
        total = total + i

print(total)

