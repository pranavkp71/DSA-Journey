# 88. Merge Sorted Array

# Q) You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# he final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



class Solution:
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
        print(nums1)
            





obj = Solution()
print(obj.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))