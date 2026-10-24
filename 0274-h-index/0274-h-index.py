from collections import defaultdict


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Since a researcher has n papers, their h-index can never exceed n.
        Being cited k times s.t. k >= n => treated as n citations.
        """
        num_papers = len(citations)
        # citation_buckets[i] = num of papers with i citations
        citation_buckets = [0] * (num_papers + 1)

        for citation in citations:
            if citation >= num_papers:
                citation_buckets[num_papers] += 1
            else:
                citation_buckets[citation] += 1

        total_papers = 0
        for i in range(num_papers, -1, -1):
            total_papers += citation_buckets[i]
            if total_papers >= i:
                return i

        return 0 
