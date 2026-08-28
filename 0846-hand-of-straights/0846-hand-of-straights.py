class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        
        for num in hand:
            start = num
            # go to the first possible card in consecutive sequence; must be the start of a group
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start] > 0:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1

        return True