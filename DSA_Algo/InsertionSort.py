def insertionSort(arr):
    for i in range(1, len(arr)):
        position = i
        currentValue = arr[i]
        #Shifting value: rightSide
        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position - 1]
            position = position - 1
        #inserting : Insertion Sort 
        arr[position] = currentValue
        print(arr)


db = [1,5,4,7,2,3,9,8] 
insertionSort(db)

#Time Complexity: O(n*2)
#Uses: Insertion sort is used when number of elements is small.
#It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.