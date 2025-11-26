class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0     # 今の層の終端
        farthest = 0        # 次に届く最も遠い場所

        for i in range(0, n - 1):
            farthest = max(farthest, i + nums[i])
            
            # 現在の層を抜けたときにジャンプが必要
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # もしもう最後まで届くなら終了
                if current_end >= n - 1:
                    break

        return jumps

solution = Solution()
print(solution.jump([2,3,1,1,4]))
print(solution.jump([2,3,0,1,4]))
print(solution.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))