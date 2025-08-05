def find_min_number(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] <  smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest
    
def selection_sort(arr):
    sorted_list = []
    while arr:
        smallest_number = find_min_number(arr)
        sorted_list.append(smallest_number)
        arr.remove(smallest_number)
    return sorted_list
    
arr = [7,1,3,5,2,4]
print(selection_sort(arr))