def christmas_tree(num):
    """
    Prints a christmas tree in '*' for given number of lines.
    """

    for i in range(num):
        print(" "*(num-i-1)+"*"*(2*i+1)) #format each line


num = int(input("Enter number of lines :"))

christmas_tree(num)