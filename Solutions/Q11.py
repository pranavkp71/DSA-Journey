class Solution:
    def jump(self, nums) -> int:
        jump = 0
        farthest = 0
        current_end = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == current_end:
                jump += 1
                current_end = farthest
        
        return jump




obj = Solution()
print(obj.jump(nums = [2,3,1,1,4]))