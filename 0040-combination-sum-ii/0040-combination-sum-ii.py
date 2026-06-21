class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx: int, path: List[int], total: int):
            if total == target:
                res.append(path.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)

        return res 