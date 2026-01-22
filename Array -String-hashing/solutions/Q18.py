# 977. Squares of a Sorted Array

# Q) Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, nums):
        result = []

        i, j = 0, len(nums)-1

        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                result.append(nums[i] * nums[i])
                i += 1
            else:
                result.append(nums[j] * nums[j])
                j -= 1
        return result[:: -1]
    

obj = Solution()
print(obj.sortedSquares(nums=[-4,-1,0,3,10]))