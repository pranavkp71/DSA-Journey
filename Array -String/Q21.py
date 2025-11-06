# 2239. Find Closest Number to Zero

# Q) Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.


class Solution:
    def findClosestNumber(self, nums) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest





obj = Solution()
print(obj.findClosestNumber([-4,-2,1,4,8]))
            
        
        