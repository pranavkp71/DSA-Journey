class Solution:
    def longestOnes(self, nums, k):
        max_length = 0
        zeros = 0
        L = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[L] == 0:
                    zeros -= 1
                L += 1

            max_length = max(max_length, R-L+1)

        return max_length

        
        



obj = Solution()
print(obj.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))