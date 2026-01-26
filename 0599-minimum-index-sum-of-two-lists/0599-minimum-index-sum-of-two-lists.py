class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        index_sum = {}

        for i, w in enumerate(list1):
            if w in common:
                index_sum[w] = i

        for j, w in enumerate(list2):
            if w in common:
                index_sum[w] += j

        min_sum = min(index_sum.values())

        return [key for key, value in index_sum.items() if value == min_sum] 