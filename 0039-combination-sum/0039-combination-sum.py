class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        def backtrack(candidates: List[int], path: List[int], cur_sum: int):
            if cur_sum == target:
                self.res.append(path)
            if cur_sum >= target:
                return
            
            for i in range(len(candidates)):
                cur_path = path + [candidates[i]]
                backtrack(candidates[i:], cur_path, cur_sum + candidates[i])

        backtrack(candidates, [], 0)

        return self.res