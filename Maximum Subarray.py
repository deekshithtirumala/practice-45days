#Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = nums[0]
        
        for x in nums:
            current_sum = max(x, current_sum+x)
            best_sum = max(current_sum, best_sum)
            
        return best_sum
