class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i: int, path: list[int], total: int):
            if total == target:
                res.append(path.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                
                path.append(candidates[j])
                dfs(j, path, total + candidates[j])
                path.pop()

        dfs(0, [], 0)
        return res