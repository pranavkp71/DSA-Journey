class Solution:
    def maxProfit(self, prices) -> int:
        low = prices[0]
        high = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = prices[i] - low
                high = max(high, profit)
        
        return high
            






obj = Solution()
print(obj.maxProfit(prices = [7,1,5,3,6,4]))