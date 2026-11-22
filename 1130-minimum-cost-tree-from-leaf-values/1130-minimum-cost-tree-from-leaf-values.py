class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        res = 0
        stack = []  # stricly decreasing stack

        # Greedily merge small leaves into their parent node.
        # When we find a "valley" we merge it and the smaller of its neighbors
        # to calculate their parent node with the smallest product.
        # The "valley" node "disappears" and we are left with the largest values in
        # the left and right subtrees for future multiplications.

        for leaf in arr:
            # Valley leaf node found and at least one neighbor exists
            while stack and stack[-1] <= leaf:
                valley_node = stack.pop()
                # left and right neighbors exist
                if stack:
                    res += valley_node * min(stack[-1], leaf)
                # only right neighbor exists
                else:
                    res += valley_node * leaf

            stack.append(leaf)

        # Left over nodes multiply to find the top nodes
        while len(stack) > 1:
            res += stack.pop() * stack[-1]

        return res
