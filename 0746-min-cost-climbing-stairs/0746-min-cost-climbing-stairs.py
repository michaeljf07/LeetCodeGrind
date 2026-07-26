class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        EMPTY = -1
        TOP = len(cost)
        memo = [EMPTY] * TOP

        def dfs(i: int) -> int:
            if i >= TOP:
                return 0
            if memo[i] != EMPTY:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1)) 