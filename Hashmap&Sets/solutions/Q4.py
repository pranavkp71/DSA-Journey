class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        
        result = []

        for num in s1:
            if num in s2:
                result.append(num)

        return result






obj = Solution()
print(obj.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))