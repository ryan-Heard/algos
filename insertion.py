
def sort(arr):
    for i in range(1,len(arr)+1):
        arr = move_line(arr[:i]) + arr[i:]

    return arr

def move_line(arr):
    temp = arr[len(arr)-1]

    #save some steps if everything is already in order.
    if temp > arr[len(arr)-2]:
        return arr

    for j in range(len(arr)-1,0,-1):
        arr[j] = arr[j-1]

        if temp <= arr[j] and temp >= arr[j-2]:
            arr[j-1] = temp
            return arr

    #If we make it her that means that temp is the smallest.
    arr[0] = temp

    return arr
