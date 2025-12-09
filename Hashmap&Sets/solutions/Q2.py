
class Solution:
    def singleNumber(self, nums: int) -> int:
        result = 0
        for num in nums:
            result = num ^ result
        return result
            



obj = Solution()
print(obj.singleNumber(nums=[4,1,2,1,2]))


