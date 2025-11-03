# 977. Squares of a Sorted Array

# Q) Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
            print(nums)
    

obj = Solution()
print(obj.sortedSquares(nums=[-4,-1,0,3,10]))