class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        
        n = len(gas)
        diffs = []
        for i in range(n):
            diffs.append(gas[i] - cost[i])

        for i, d in enumerate(diffs):
            if d < 0:
                continue
            j = 0
            total = 0
            success = True
            while j < n:
                idx = (i + j) % n
                total += diffs[idx]
                if total < 0:
                    success = False
                    break
                j += 1
            if success:
                return i


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