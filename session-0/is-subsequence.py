def is_subsequence(subs,mains):
    """
    Checks if the characters in subsequence occur in the same order in the main sequence
    """

    main_index = 0

    for sub_index in range(len(subs)):
       
       main_index = mains.find(subs[sub_index],main_index)
       #check if the relevent subsequence character occurs in the correct place of main string
       
       if main_index == -1 :
           #character isn't found in order
           print("False")
           return False
       
       main_index = main_index + 1 #skip last matching index
       
    return True


subs = input("Subsequence :")
mains = input("Main sequence :")

print(is_subsequence(subs,mains))
