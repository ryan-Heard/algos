import math

def sort(arr):
    #check the length of each
    split_at = math.floor(len(arr)/2)
    left = arr[:split_at]
    right = arr[split_at:]

    if len(arr) > 2:
        left = sort(left)
        right = sort(right)

    return combine(left,right)

def combine(left, right):
    i = 0
    j = 0
    sorted = [];

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        elif right[j] < left[i]:
            sorted.append(right[j])
            j += 1
        else: #In case of ==
            sorted.append(left[i])
            i += 1

    #Preforms clean up
    if i < len(left):
        for elm in left[i:]:
            sorted.append(elm)
    elif j < len(right):
        for elm in right[j:]:
            sorted.append(elm)

    return sorted
