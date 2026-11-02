from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if endGene not in bank:
            return -1
        
        q = deque() # (gene, # of mutations)
        q.append((startGene, 0))
        visited = set()

        while q:
            cur_gene, cur_mutations = q.popleft()
            # we have successfully made it to the end gene
            if cur_gene == endGene:
                return cur_mutations

            for next_gene in bank:
                # if the next gene has exactly 1 different char, we can consider it
                num_chars_diff = 0
                for cur_gene_char, next_gene_char in zip(cur_gene, next_gene):
                    if cur_gene_char != next_gene_char:
                        num_chars_diff += 1
                if num_chars_diff == 1 and next_gene not in visited:
                    q.append((next_gene, cur_mutations + 1))
                    visited.add(next_gene)

        return -1
