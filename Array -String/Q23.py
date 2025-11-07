# 238. Product of Array Except Self

# Q) Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        l_multi = 1
        r_multi = 1

        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1
            l_arr[i] = l_multi
            r_arr[j] = r_multi

            l_multi *= nums[i]
            r_multi *= nums[j]

            print(l_multi, r_multi)

        return [l_arr[i] * r_arr[i] for i in range(n)]


        



obj = Solution()
print(obj.productExceptSelf(nums=[1,2,3,4]))