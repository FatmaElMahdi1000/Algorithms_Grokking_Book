print("*******************NORMAL WAY! ****************************")
def FirstFactorial(num):
    if num == 1 or num == 0:
        return 1
    elif num > 18:
        return "ERROR"
    num_combinations = []
    for i in range(num, 0, -1):
        num_combinations.append(i)
    Factorial_product = 1
    for i in num_combinations:
        Factorial_product = Factorial_product * i #Factorial_product *= i
    return Factorial_product
    

# keep this function call here 
print(FirstFactorial(4))

print("*******************REVURSIVE WAY! ****************************")

def FirstFactorial(num):
    digits_list = [num]
    while num > 1:
        num = num - 1
        digits_list.append(num)
        FirstFactorial(num)
    return digits_list
    
def Factorial_output(digits_list):
    result = 1
    for i in digits_list:
        result *= i
    return result
    
lst = FirstFactorial(4)
print(lst)
print(Factorial_output(lst))







