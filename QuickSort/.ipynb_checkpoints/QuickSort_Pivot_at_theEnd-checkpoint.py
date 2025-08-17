def quick_sort(arr):
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    less = []
    greater = [] 
    pivot = arr[-1]
    for num in arr[0:-1]:
        if num > pivot:
            greater.append(num)
        elif num < pivot:
            less.append(num)
    return quick_sort(less) + [pivot] + quick_sort(greater)
    
arr = [4,3,1,2,5,9,7,10,6,3] 
print(quick_sort(arr))