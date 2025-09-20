# 238. Product of Array Except Self

# Q) Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]
    


obj = Solution()
print(obj.productExceptSelf(nums=[1,2,3,4]))


        