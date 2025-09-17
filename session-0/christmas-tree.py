##Christmas tree
def christmas_tree(num):
    for i in range(num):
        print(" "*(num-i-1)+"*"*(2*i+1))

num = int(input("Enter number of lines :"))

christmas_tree(num)