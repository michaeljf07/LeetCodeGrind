class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        words = set(wordList)
        res = 0
        q = deque([beginWord])

        alph_ascii_lower = 97
        alph_ascii_higher = 123

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res

                for i in range(len(node)):
                    for c in range(alph_ascii_lower, alph_ascii_higher):
                        if chr(c) == node[i]:
                            continue

                        nei = node[:i] + chr(c) + node[i + 1:]

                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0 