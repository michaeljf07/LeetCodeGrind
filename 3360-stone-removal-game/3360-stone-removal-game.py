class Solution:
    def canAliceWin(self, n: int) -> bool:
        # if there are less than 10 stones, Alice cannot go
        if n < 10:
            return False

        stones_removed = 10
        n -= stones_removed # Alice's first turn
        alice_wins = True
        while n > 0:
            stones_removed -= 1
            if stones_removed > n:
                return alice_wins

            n -= stones_removed
            alice_wins = not alice_wins

        return alice_wins