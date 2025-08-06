print("#***********Brute force SOLUTION (using nested loops - slower solutions in terms of the running time (o(n^2))***********************#")
class Solution(object):
    def twoSum(self, nums, target):
        nums_length = len(nums)
        if not (2 <= nums_length <= 10**4):
            return "ERROR: Invalid Array"
        else:
            for i in range(0, nums_length):
                for j in range(i + 1, nums_length):
                    if nums[i] + nums[j] == target:
                        return i, j
            return -1 #no 2 numbers can add up to the target.

#return indcies of 2 numbers 7 + 2 = 9 
nums = [2,7,11,15]
target = 9
result = Solution()
Final = result.twoSum(nums, target)
print(Final)
print("#***********HASH TABLE SOLUTION***********************#")
class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        nums_length = len(nums)
        if not (2 <= nums_length <= 10**4):
            return "ERROR: Invalid Array"
        else:
            for index, num in enumerate(nums):
                complement_number = target - num
                if complement_number in hash_table:
                    return [hash_table[complement_number], index]
                hash_table[num] = index
                

nums = [2,7,11,15]
target = 9
result = Solution()
Final = result.twoSum(nums, target)
print(Final)







