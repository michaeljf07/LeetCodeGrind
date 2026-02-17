class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_index = {}
        for friend in friends:
            friend_index[friend] = order.index(friend)
        
        sorted_items = sorted(friend_index.items(), key=lambda item: item[1])
        
        return [item[0] for item in sorted_items]
