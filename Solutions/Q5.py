class Solution:
    def removeDuplicates(self, nums) -> int:
       if len(nums) <= 2:
           return len(nums)
       
       k = 2

       for i in range(2, len(nums)):
           if nums[i] != nums[k-2]:
               nums[k] = nums[i]
               k += 1
            
       return k








obj = Solution()
print(obj.removeDuplicates(nums = [1,1,1,2,2,3]))