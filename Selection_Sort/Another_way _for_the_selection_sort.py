def selection_sort(arr):
    if not arr: #base case 
        return []
        
    sorted_arr = []
    copied_arr = arr.copy()
    min_number = arr[0]
    for num in arr:
        if num < min_number:
            min_number = num
    sorted_arr.append(min_number)
    copied_arr.remove(min_number)
    
    return [min_number] + selection_sort(copied_arr)
    

arr = [12, 3, 1, 16, 0]
print(selection_sort(arr))