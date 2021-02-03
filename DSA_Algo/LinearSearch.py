#UNORDERED LIST
#random, not fixed length
x = [10, 1, 5, 93, 51, 7, 16]

#Algo: LinearSearch or SequentialSearch
def SequentialSearch(arr, item):
    position = 0 
    found = False

    while position < len(arr) and not found:
        if x[position] == item:
            found = True
            print("Found the Item.")
        else:
            position+=1
            
    return found


SequentialSearch(x, 1)

#The complexity of Linear Search Technique
#Time Complexity: O(n)
#Space Complexity: O(1)