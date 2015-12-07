import math

def find_match(arr, value):
    low = 0;
    high = len(arr)
    mid = math.floor((high-low)/2)

    if arr[mid] == value:
        print("Found")
        return True
    elif arr[mid] > value:
        high = mid
    elif arr[mid] < value:
        low = mid

    if len(arr) == 1:
        print("Not Found")
        return False

    mid = math.floor((high-low)/2)

    find_match(arr[low:high], value)
