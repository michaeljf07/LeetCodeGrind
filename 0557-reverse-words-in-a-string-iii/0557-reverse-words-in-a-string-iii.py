class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        answer = []
        for i in s:
            answer.append(i[::-1])
            
        return " ".join(answer)