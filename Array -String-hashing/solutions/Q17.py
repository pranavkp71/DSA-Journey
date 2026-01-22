# 283. Move Zeroes

# Q) Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums) -> None:
       j = 0
       for i in range(len(nums)):
               if nums[i] != 0:
                   nums[j], nums[i] = nums[i], nums[j]
                   j += 1
       return nums
                    



obj = Solution()
print(obj.moveZeroes(nums=[0,1,0,3,12]))
        