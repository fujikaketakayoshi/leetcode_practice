class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # 1. 重複を効果的に処理するために、まず候補をソートします
        candidates.sort()
        results = []

        # start_index: 次の要素をどこから探し始めるか
        # current_sum: 現在の組み合わせの合計
        # current_combinations: 現在構築中の組み合わせ
        def dfs(start_index, current_sum, current_combinations):
            if current_sum == target:
                # ターゲットに到達したら、結果に追加して終了
                results.append(list(current_combinations))
                return
            
            # current_sum > target のチェックは、ループ内で break を使うため省略可能ですが、
            # 再帰の冒頭に記述しても問題ありません。
            # if current_sum > target:
            #     return

            for i in range(start_index, len(candidates)):
                # ★ 2. 重複する組み合わせを防ぐ処理 ★
                # 同じレベルの再帰（現在のforループ）で、同じ値の要素を重複して開始点にしない
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                val = candidates[i]
                
                # 枝刈り：合計がターゲットを超えることが確定したら、それ以降の候補も超えるためループを終了
                if current_sum + val > target:
                    break
                
                # 選択
                current_combinations.append(val)
                
                # 次の再帰呼び出し
                # i + 1: 同じ要素を再利用しないため、次のインデックスから探索を開始
                dfs(i + 1, current_sum + val, current_combinations)
                
                # ★ 1. バックトラック（状態の復元） ★
                # 再帰から戻ったら、現在の要素を組み合わせと合計値から削除して状態を元に戻す
                current_combinations.pop()
        
        # 探索開始
        dfs(0, 0, [])
        return results

Solution = Solution()
print(Solution.combinationSum2([10,1,2,7,6,1,5], 8))
