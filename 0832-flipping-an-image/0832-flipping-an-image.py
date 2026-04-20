class Solution:
    def invert(self, num: int) -> bool:
        if num == 0:
            return 1
        else:
            return 0

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for row in image:
            inverted = list(map(lambda x: self.invert(x), row))
            inverted.reverse()
            res.append(inverted)
        
        return res

        