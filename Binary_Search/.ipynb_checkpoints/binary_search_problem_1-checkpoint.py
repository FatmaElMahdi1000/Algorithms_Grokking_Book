def binary_sort(arr, item):
    """
    objective of the function: takes array/sorted list, to find index of a given item

    paramaters: 
    arr (list):A list of elements sorted in ascending order.
    item (any): the value to search for and return its index

    Returns:
    int: index of the item 
    """
    firstNo_index = 0
    lastNo_index = len(arr) - 1
    while firstNo_index <= lastNo_index:  #iteration#1: 0 < 6
        No_inTheMid_index = lastNo_index + firstNo_index // 2 #// floor division, when number is odd it rounds it down. 
        Guess = arr[No_inTheMid_index]
        if Guess == item:
            return No_inTheMid_index
        elif Guess < item:
            firstNo_index = No_inTheMid_index + 1
        elif Guess > item:
            lastNo_index = No_inTheMid_index - 1
        else:
            return None, "item does not exist"
            

#arry =[0, ..., len(arr)-1 (7-1)]
arr = [1, 4, 6, 9 , 11, 15, 20]
item = 9
result = binary_sort(arr, item)
print(result) 