# 283. Move Zeroes

# Q) Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.



class Solution:
    def moveZeroes(self, nums) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

        print(nums)
                
            




obj = Solution()
print(obj.moveZeroes(nums=[0,1,0,3,12]))
        