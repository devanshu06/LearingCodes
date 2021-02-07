################################################################################## BUBBLE SORT #######################################################################
def BubbleSort(data):        
    swap = False        # Creating a Swap Varaiable 
    for f in range(len(data)-1):                 # getting all the value of data in the f variable
        for s in range(len(data) - 1 - f):       # creting the S variable for comparing the data                 
            if data[s] > data[s+1]:              
                data[s], data[s+1] = data[s+1], data[s]
                swap == True                
                print("Swap Done")
                print("The data after swapping: ", data)
            if swap == False:    
                print("The Sorted data: ", data)

db = [25,69,83,512,54,67,12,53]
BubbleSort(db)


