class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            current_tank += gain

            if current_tank < 0:
                start = i + 1
                current_tank = 0

        return start if total_tank >= 0 else -1


obj = Solution()
print(obj.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))