class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        num_needs = len(needs)
        memo: dict[tuple[int, ...], int] = {} # (needs) -> min_price

        def dfs(curr_needs: tuple[int, ...]) -> int:
            if curr_needs in memo:
                return memo[curr_needs]

            # base price if you use no more specials
            min_price = sum(curr_needs[i] * price[i] for i in range(num_needs))

            for offer in special:
                if all(offer[i] <= curr_needs[i] for i in range(num_needs)):
                    # apply the special
                    new_needs = tuple(curr_needs[i] - offer[i] for i in range(num_needs))
                    # recurse through the decision tree by finding the min of no specials
                    # and applying each special
                    min_price = min(min_price, offer[-1] + dfs(new_needs))

            memo[curr_needs] = min_price
            return min_price

        return dfs(tuple(needs))
