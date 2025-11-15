# 189. Rotate Array

# Q) Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        i, j = 0, n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        i, j = k, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        return nums

            

       



obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], 3))
        