class Solution:
    def containsDuplicate(self, nums) -> bool:
        l = set()
        for num in nums:
            if num in l:
                return True
            else:
                l.add(num)
        return False




obj = Solution()
print(obj.containsDuplicate(nums=[1,2,3,1]))
        