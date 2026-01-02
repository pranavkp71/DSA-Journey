class Solution:
    def findClosestNumber(self, nums) -> int:
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest




obj = Solution()
print(obj.findClosestNumber(nums=[2,-1,1]))
        