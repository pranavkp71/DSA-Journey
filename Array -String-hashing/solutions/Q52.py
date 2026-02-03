class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                current = num
                streak = 1
            while current + 1 in s:
                current += 1
                streak += 1
            
            longest = max(longest, streak)

        return longest




obj = Solution()
print(obj.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
