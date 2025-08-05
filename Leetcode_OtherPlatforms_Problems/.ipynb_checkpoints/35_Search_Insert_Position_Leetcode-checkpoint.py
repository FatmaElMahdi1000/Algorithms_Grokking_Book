class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_length = len(nums)
        if not isinstance(target, int) or not (-10**4) <= target <= (10**4):
            return "ERORR: INVALID TARGET TO LOOK FOR!"
        if not 1 <= num_length <= (10**4):
            return "ERORR:nums is OUT OF RANGE!"
        low_index = 0
        high_index = num_length - 1
        while low_index <= high_index:
            mid_index = (high_index + low_index) // 2 
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                low_index = mid_index + 1
            elif nums[mid_index] > target:
                high_index = mid_index - 1
        return nums[:low_index] + [target] + nums[low_index:]
        
                
        """if target not in nums:
            nums.sort()
            for i, num in enumerate(nums):
                if num > target:
                    left = nums[0:i]
                    right = nums[i:]
                    return left + [target] + right"""
                    
nums = [1,3,5,6]
target = 4
Result = Solution()
Final = Result.searchInsert(nums, target)
print(Final) 