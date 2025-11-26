class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 1. 重複排除と枝刈りのため、candidatesをソート
        candidates.sort()
        
        results = []
        
        def dfs(start_index: int, current_sum: int, current_combination: list[int]):
            # ベースケース 1: 目標値に達した場合
            if current_sum == target:
                # 目標値に達した組み合わせを結果に追加
                # combinationをコピーして追加することが重要
                results.append(list(current_combination))
                return
            
            # ベースケース 2: 目標値を超えた場合 (探索を打ち切る/枝刈り)
            if current_sum > target:
                return

            # start_indexから探索を開始
            # これにより、[2, 3] と [3, 2] のような順序違いによる重複を排除
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # 枝刈り（Optimization/Pruning）: 
                # ソートされているため、現在の要素を追加するとtargetを超える場合、
                # それ以降の要素も必ずtargetを超えるため、ループを中断
                if current_sum + candidate > target:
                    break
                
                # 選択
                current_combination.append(candidate)
                
                # 再帰呼び出し (DFS)
                # 同じ要素を再度使用できるため、iではなくiをstart_indexとして渡す
                dfs(i, current_sum + candidate, current_combination)
                
                # バックトラック
                # 次のループのために、追加した要素を元に戻す
                current_combination.pop()

        # 探索開始
        # 初期インデックス: 0, 初期合計: 0, 初期組み合わせ: []
        dfs(0, 0, [])
        return results

Solution = Solution()
print(Solution.combinationSum([1,2,3,4,5,6,7,8,9,10], 10))