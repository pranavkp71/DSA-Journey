
class Solution:
    def containsDuplicate(self, nums: int) -> bool:
        sett = set()
        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        return False


obj = Solution()
print(obj.containsDuplicate(nums=[1,2,3,4]))

