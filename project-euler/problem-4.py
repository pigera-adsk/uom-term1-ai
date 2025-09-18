def check_palindrome(sequence):
    """
    Check if a given string is a palindrome
    """

    sequence = sequence.strip()
    if sequence == sequence[::-1]:
        return True
    return False


num1 = 999
num2 = 999
multiplied = []

while num1>=100:
    while num2>=100:
        multiplied.append(num1*num2)
        num2 = num2-1
    num1 = num1 - 1
    num2 = num1

multiplied.sort(reverse=True)

for num in multiplied:
    if check_palindrome(str(num)):
        print(num)
        break