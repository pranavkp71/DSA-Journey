class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        h = 0

        for i in range(len(citations)-1):
            if citations[i] >= i+1:
                h = i+1
        
        return h
        










obj = Solution()
print(obj.hIndex(citations = [3,0,6,1,5]))