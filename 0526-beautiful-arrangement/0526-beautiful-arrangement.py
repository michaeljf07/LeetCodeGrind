class Solution:
    def countArrangement(self, n: int) -> int:
        # used[i] = whether i has been used in the permutation
        used = [False] * (n + 1)

        def backtrack(idx: int) -> int:
            # built a permutation
            if idx > n:
                return 1

            count = 0
            # P(n, n) must use all [1, n] numbers
            for i in range(1, n + 1):
                if not used[i]:
                    if i % idx == 0 or idx % i == 0:
                        used[i] = True  # use number in permutation
                        count += backtrack(idx + 1)
                        used[i] = False  # backtack

            return count

        return backtrack(1)
