"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4 """
class Solution(object):
    def search(self, nums, target):
        low_idx = 0 #low index 
        high_idx = len(nums) - 1   #high_index
        while low_idx <= high_idx:
            mid_idx = (high_idx + low_idx) // 2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                low_idx = mid_idx + 1
            elif nums[mid_idx] > target:
                high_idx = mid_idx - 1
        return None
            
            

nums = [-1,0,3,5,9,12]
target = 9
Result  = Solution()
Result = Result.search(nums, target)
print(Result)