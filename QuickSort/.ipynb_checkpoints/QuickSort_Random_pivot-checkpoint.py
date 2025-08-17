from random import choice

def Quick_sort(arr):
    if len(arr) <= 1:  ##Base Case, Review this
        return arr
    else:
        pivot = choice(arr)
        copied_arr = arr.copy()
        copied_arr.remove(pivot)
        
        smaller_elements = []
        greater_elements = []
        
        for num in copied_arr:
            if num > pivot:
                greater_elements.append(num)
            else:
                smaller_elements.append(num)
        return Quick_sort(smaller_elements) + [pivot] + Quick_sort(greater_elements)  #Recursive call
arr = [12, 3, 1, 18, 0, 2]
print(Quick_sort(arr))
