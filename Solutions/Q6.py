class Solution:
    def majorityElement(self, nums) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            
            else:
                count -= 1

        return candidate






obj = Solution()
print(obj.majorityElement(nums=[3,2,3]))