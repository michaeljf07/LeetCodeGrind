class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # stores (string, num_to_repeat)
        cur_str = ""
        cur_num_to_repeat = 0

        for char in s:
            if char == '[':
                stack.append((cur_str, cur_num_to_repeat))
                cur_str = ""
                cur_num_to_repeat = 0
            elif char == ']':
                prev_str, num_to_repeat = stack.pop()
                cur_str = prev_str + cur_str * num_to_repeat
            elif char.isdigit():
                cur_num_to_repeat = cur_num_to_repeat * 10 + int(char)
            else:
                cur_str += char

        return cur_str