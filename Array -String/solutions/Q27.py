# 209. Minimum Size Subarray Sum

# Q) Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        min_length = float('inf')
        cur_sum = 0
        L = 0

        for R in range(len(nums)):
            cur_sum += nums[R]

            while cur_sum >= target:
                min_length = min(min_length, R-L+1)
                cur_sum -= nums[L]
                L += 1
        
        return min_length if min_length < float('inf') else 0

        




obj = Solution()
print(obj.minSubArrayLen(nums=[2,3,1,2,4,3], target=7))