# 219. Contains Duplicate II

# Q) Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        seen = set()
        j = 0

        for i in range(len(nums)):
            if i - j > k:
                seen.remove(nums[j])
                j += 1
            if nums[i]in seen:
                return True
            seen.add(nums[i])
        return False




obj = Solution()
print(obj.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k = 2))
        