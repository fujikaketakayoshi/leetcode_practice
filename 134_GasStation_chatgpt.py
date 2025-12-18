class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # i までは全部ダメ
                start = i + 1
                tank = 0

        return start

solution = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(solution.canCompleteCircuit(gas, cost))  # 出力: 3
gas = [2,3,4]
cost = [3,4,3]
print(solution.canCompleteCircuit(gas, cost))  # 出力: -1
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(solution.canCompleteCircuit(gas, cost))  # 出力: 4
