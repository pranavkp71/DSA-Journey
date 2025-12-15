class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        sorted_item = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_item[i][0])
        
        return result
            

        




obj = Solution()
print(obj.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

