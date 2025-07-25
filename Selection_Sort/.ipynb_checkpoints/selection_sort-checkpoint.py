"""🔁 Visual analogy
Think of your code like this:

return inside a loop = 🔚 "Exit the function NOW"

print inside a loop = 📢 "Say something, then continue the loop"""

def find_the_smallest(arr):
    sorted_list = []
    arr = arr.copy()
    i = 1
    while arr:
        minimum_num = min(arr)
        sorted_list.append(minimum_num)
        arr.remove(minimum_num)
        i += 1
        print (f"ITERATION #{i} unsorted_list = {arr} and sorted_list = {sorted_list}")
    return f"Final_ sorted_list = {sorted_list}"

arr = [2,5,10,1,0]
print(find_the_smallest(arr))