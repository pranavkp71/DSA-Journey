# 643. Maximum Average Subarray I

# Q) You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.


class Solution:
    def findMaxAverage(self, nums, k) -> float:
        cur_sum = 0
        n = len(nums) - 1
        
        for i in range(k):
            cur_sum += nums[i]
        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            avg = cur_sum / k
            max_avg = max(max_avg, avg)
        
        return max_avg




obj = Solution()
print(obj.findMaxAverage(nums=[1,12,-5,-6,50,3], k = 4))