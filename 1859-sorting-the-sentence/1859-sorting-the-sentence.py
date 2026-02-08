class Solution:
    def sortSentence(self, s: str) -> str:
        split_sentence = s.split()
        len_sentence = len(split_sentence)

        ans = [""] * len_sentence

        for word in split_sentence:
            idx = int(word[-1])
            ans[idx - 1] = word[:-1]

        return " ".join(ans)
        