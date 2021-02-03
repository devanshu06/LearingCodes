#Binary Search Algorithm
def bs(db, value):                                              #Starting the binary search function
    start = 0                                                   #String Pointer value is 0
    end = db[-1]                                                #End Pointer value is the last value of the list    
    middle = int((start + end)/2)                               #creating middle value
    print("Start: ", start, "Middle:", middle, "End:", end)     
    while not(value == middle) and start <= end:                #not(value == middle) ----> not(False) ----> True    
        if value > middle:                                      #start pointer will be noe (middle + 1)th position                    
            start = middle + 1
            middle = int((start + end)/2)
            print("Start: ", start, "Middle:", middle, "End:", end)
        else:                                                   # if user value is less than the middle value    
            end = middle - 1                                    #then end pointer will now (middle - 1)th position    
            middle = int((start + end)/2)
            print("Start: ", start, "Middle:", middle, "End:", end)
    if value == middle:                                         #if the user value is equivalent to middle value then we have found the required value
        print("We have Found.")                                                         
    else:                                                       #if the value is not present in the list then we are unable to find the value                     
        print("Not Found.")
        print("Start: ", start, "Middle:", middle, "End:", end)

#Calling the Binary Search Algorithm
bs(list(range(11)), 25)

bs(list(range(11)), 6)


#The time complexity of the binary search algorithm is O(log n). 
#The best-case time complexity would be O(1)
#The worst-case scenario could be the values at either extremity of the list or values not in the list. 