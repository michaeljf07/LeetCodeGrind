class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [[-1, -1] for _ in range(len(nums))]

        def dfs(house: int, robbed_first: bool) -> int:
            if (house >= len(nums)) or (robbed_first and house == len(nums) - 1):
                return 0
            
            if memo[house][robbed_first] != -1:
                return memo[house][robbed_first]
            
            memo[house][robbed_first] = max(
                dfs(house + 1, robbed_first),
                nums[house] + dfs(house + 2, robbed_first)
            )

            return memo[house][robbed_first]

        return max(dfs(0, True), dfs(1, False)) 