class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        new_num = 0
        for digit in num:
            new_num = new_num * 10 + digit
        
        new_num += k

        return [int(d) for d in str(new_num)]