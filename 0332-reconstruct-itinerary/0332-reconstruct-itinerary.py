from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                # Reached dead end => this airport is finished
                res.append(stack.pop())
            else:
                # Flights are still available: advance along the next flight
                stack.append(adj[curr].pop())

        return res[::-1]
                
