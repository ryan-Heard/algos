import sys
import os
import selection
import merge
import insertion

def main():
    list = [10,1,12,23,44,5,67,27,8,9,10,11]
    list_b = [10,1,12,23,44,5,67,27,8,9,10,11]
    list_c = [1,2,4,5,3]

    print(insertion.sort(list))
    print(list_b)
    print("Sorted! ")

main()
