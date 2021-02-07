def BubbleSort(data):
    for f in range(len(data)-1):
        print("First Data: ", f)
        for s in range(len(data)-1-f):
            print("Second data: ", s)
            if data[s] > data[s+1]:
                data[s], data[s+1] = data[s+1], data[s]
                print("Swap Done")
        print("Pass Completed")
        print("Every Pass result: ", data)
    return data 

db = [10, 55, 94, 13, 58]
BubbleSort(db)