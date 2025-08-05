def selection_sort(arr):
    sorted_list = []
    while arr:
        min_value = min(arr)
        sorted_list.append(min_value)
        arr.remove(min_value)
    return sorted_list


arr = [7,1,3,5,2,4]
print(selection_sort(arr))