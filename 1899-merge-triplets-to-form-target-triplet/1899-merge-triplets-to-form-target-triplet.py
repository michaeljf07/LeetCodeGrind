class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = set()
        for triplet in triplets:
            # if triplet[i] > target[i] it can be discarded
            if not self.isTripletValid(triplet, target):
                continue
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    possible.add(i)
        
        return len(possible) == 3

    @staticmethod
    def isTripletValid(triplet: List[List[int]], target: List[int]) -> bool:
        return (
            triplet[0] <= target[0] and
            triplet[1] <= target[1] and
            triplet[2] <= target[2]
        ) 