#Largest palindrome product of 3-digit numbers

def check_palindrome(sequence):
    """
    Check if a given string is a palindrome
    """

    sequence = sequence.strip()
    if sequence == sequence[::-1]:
        return True
    return False


start = 100
limit = 999

num1 = limit
num2 = limit
multiplied = []

#Loop gets all products of 3-digit numbers
while num1>=start:
    while num2>=start:
        multiplied.append(num1*num2)
        num2 = num2-1
    num1 = num1 - 1
    num2 = num1

multiplied.sort(reverse=True) #Sort products from largest to smallest

for num in multiplied:
    if check_palindrome(str(num)):
        print(num)
        break


#Time Complexity O(n^2) (n=limit-start)
#Space Complexity O(n^2)